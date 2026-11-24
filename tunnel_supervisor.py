#!/usr/bin/env python3
"""
OfficerPass Dual-Tunnel Supervisor
Keeps https://officerpass-vashishta.loca.lt active 24/7 with automatic restart on sleep/disconnect.
Simultaneously runs a Cloudflare tunnel as an instant fallback.
"""

import subprocess
import time
import re
import sys
import os
import threading
import json

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
os.makedirs(DATA_DIR, exist_ok=True)
TUNNEL_FILE = os.path.join(DATA_DIR, 'live_tunnel.json')

state = {
    'localtunnel': 'https://officerpass-vashishta.loca.lt',
    'localtunnel_status': 'starting',
    'cloudflare': None,
    'cloudflare_status': 'starting',
    'last_updated': time.time()
}

def save_state():
    try:
        with open(TUNNEL_FILE, 'w') as f:
            json.dump(state, f, indent=2)
    except Exception as e:
        print(f"[SUPERVISOR] Error saving state: {e}", flush=True)

def run_localtunnel():
    cmd = ["npx", "--yes", "localtunnel", "--port", "8080", "--subdomain", "officerpass-vashishta"]
    while True:
        print(f"[LOCALTUNNEL] Starting tunnel for officerpass-vashishta at {time.strftime('%H:%M:%S')}...", flush=True)
        try:
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
            state['localtunnel_status'] = 'running'
            save_state()
            
            while True:
                line = proc.stdout.readline()
                if not line:
                    break
                line_str = line.strip()
                if "your url is" in line_str.lower():
                    print(f"[LOCALTUNNEL] *** FIXED URL ACTIVE ***: https://officerpass-vashishta.loca.lt", flush=True)
                    state['localtunnel_status'] = 'connected'
                    save_state()
                elif "tunnel error" in line_str.lower() or "connection closed" in line_str.lower():
                    print(f"[LOCALTUNNEL] Disconnect notice: {line_str[:80]}", flush=True)
            
            proc.terminate()
            proc.wait(timeout=3)
        except Exception as e:
            print(f"[LOCALTUNNEL] Exception: {e}", flush=True)
        
        print("[LOCALTUNNEL] Process exited. Auto-restarting in 2 seconds...", flush=True)
        state['localtunnel_status'] = 'reconnecting'
        save_state()
        time.sleep(2)

def run_cloudflare():
    cmd = ["/opt/homebrew/bin/cloudflared", "tunnel", "--url", "http://localhost:8080"]
    while True:
        print(f"[CLOUDFLARE] Starting fallback tunnel at {time.strftime('%H:%M:%S')}...", flush=True)
        try:
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
            state['cloudflare_status'] = 'running'
            
            while True:
                line = proc.stdout.readline()
                if not line:
                    break
                line_str = line.strip()
                match = re.search(r'https://[a-zA-Z0-9-]+\.trycloudflare\.com', line_str)
                if match:
                    url = match.group(0)
                    state['cloudflare'] = url
                    state['cloudflare_status'] = 'connected'
                    save_state()
                    print(f"[CLOUDFLARE] Live fallback URL: {url}", flush=True)
                
                if "Tunnel not found" in line_str or "datagram manager error" in line_str:
                    print(f"[CLOUDFLARE] Dead tunnel detected. Restarting...", flush=True)
                    break
            
            proc.terminate()
            proc.wait(timeout=3)
        except Exception as e:
            print(f"[CLOUDFLARE] Exception: {e}", flush=True)
        
        print("[CLOUDFLARE] Process exited. Auto-restarting in 3 seconds...", flush=True)
        state['cloudflare_status'] = 'reconnecting'
        save_state()
        time.sleep(3)

if __name__ == '__main__':
    t1 = threading.Thread(target=run_localtunnel, daemon=True)
    t2 = threading.Thread(target=run_cloudflare, daemon=True)
    t1.start()
    t2.start()
    
    # Keep main thread alive
    while True:
        time.sleep(1)
