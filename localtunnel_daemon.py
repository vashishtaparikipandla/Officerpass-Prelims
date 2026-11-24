#!/usr/bin/env python3
"""
OfficerPass Localtunnel Permanent Supervisor
Ensures https://officerpass-vashishta.loca.lt is ALWAYS bound and serving 24/7.
"""

import subprocess
import time
import urllib.request
import os
import signal
import sys

URL = "https://officerpass-vashishta.loca.lt"
SUBDOMAIN = "officerpass-vashishta"
PORT = "8080"
LOG_FILE = "/tmp/officerpass_localtunnel.log"

def check_health():
    """Returns True if the tunnel responds with 200 OK, False otherwise."""
    try:
        req = urllib.request.Request(
            URL,
            headers={
                "User-Agent": "OfficerPassWatchdog/1.0",
                "Bypass-Tunnel-Reminder": "true"
            }
        )
        with urllib.request.urlopen(req, timeout=5) as resp:
            return resp.status == 200
    except Exception:
        return False

def get_assigned_url():
    """Reads /tmp/officerpass_localtunnel.log to check what URL localtunnel got."""
    if not os.path.exists(LOG_FILE):
        return None
    try:
        with open(LOG_FILE, 'r') as f:
            content = f.read()
            for line in content.splitlines():
                if "your url is:" in line.lower():
                    return line.split("your url is:")[-1].strip()
    except Exception:
        pass
    return None

def main():
    print(f"[WATCHDOG] Permanent Localtunnel Supervisor starting for {URL}...", flush=True)
    
    while True:
        # Start localtunnel
        with open(LOG_FILE, "w") as log_f:
            proc = subprocess.Popen(
                ["npx", "--yes", "localtunnel", "--port", PORT, "--subdomain", SUBDOMAIN],
                stdout=log_f,
                stderr=log_f
            )
        
        # Wait up to 5 seconds to see what URL was assigned
        assigned = None
        for _ in range(5):
            time.sleep(1)
            assigned = get_assigned_url()
            if assigned:
                break
        
        print(f"[WATCHDOG] loca.lt assigned: {assigned}", flush=True)
        
        if not assigned or SUBDOMAIN not in assigned:
            print(f"[WATCHDOG] Warning: Did not get desired subdomain '{SUBDOMAIN}' (got {assigned}). Retrying in 4s...", flush=True)
            try:
                proc.terminate()
                proc.wait(timeout=3)
            except Exception:
                proc.kill()
            time.sleep(4)
            continue
        
        # Verify HTTP response
        verified = False
        for _ in range(5):
            if check_health():
                verified = True
                print(f"[WATCHDOG] *** VERIFIED LIVE ***: {URL} is responding (HTTP 200)", flush=True)
                break
            time.sleep(1.5)
        
        if not verified:
            print("[WATCHDOG] Healthcheck failed on assigned URL. Restarting...", flush=True)
            try:
                proc.terminate()
                proc.wait(timeout=3)
            except Exception:
                proc.kill()
            time.sleep(3)
            continue
        
        # Active monitor loop
        failures = 0
        while True:
            time.sleep(15)
            
            # Check process state
            if proc.poll() is not None:
                print(f"[WATCHDOG] localtunnel exited with code {proc.returncode}. Restarting...", flush=True)
                break
            
            # Check endpoint
            if check_health():
                failures = 0
            else:
                failures += 1
                print(f"[WATCHDOG] Health ping missed ({failures}/2)...", flush=True)
                if failures >= 2:
                    print(f"[WATCHDOG] 2 consecutive failures on {URL}. Re-spawning...", flush=True)
                    break
        
        # Cleanup before restart
        try:
            proc.terminate()
            proc.wait(timeout=3)
        except Exception:
            try:
                proc.kill()
            except Exception:
                pass
        
        time.sleep(2)

if __name__ == "__main__":
    main()
