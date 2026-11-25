const localtunnel = require('localtunnel');
const https = require('https');

const PORT = 8080;
const SUBDOMAIN = 'officerpass-vashishta';
const HOST = 'https://loca.lt';
const EXPECTED_URL = `https://${SUBDOMAIN}.loca.lt`;
const HEALTH_CHECK_INTERVAL_MS = 60000;
const HEALTH_CHECK_TIMEOUT_MS = 15000;

process.on('uncaughtException', (err) => {
  console.warn('[PERMA-TUNNEL] Caught uncaughtException:', err.message || err);
});

process.on('unhandledRejection', (reason) => {
  console.warn('[PERMA-TUNNEL] Caught unhandledRejection:', reason);
});

function checkTunnelHealth() {
  return new Promise((resolve) => {
    const req = https.get(
      EXPECTED_URL,
      {
        headers: { 'Bypass-Tunnel-Reminder': 'true' },
        timeout: HEALTH_CHECK_TIMEOUT_MS
      },
      (res) => {
        if (res.statusCode < 500) {
          resolve(true);
        } else {
          console.warn(`[PERMA-TUNNEL] Health-check status ${res.statusCode} (${res.headers['x-localtunnel-status'] || 'Unknown'})`);
          resolve(false);
        }
      }
    );

    req.on('error', (err) => {
      console.warn('[PERMA-TUNNEL] Health-check request error:', err.message);
      resolve(false);
    });

    req.on('timeout', () => {
      req.destroy();
      console.warn('[PERMA-TUNNEL] Health-check request timed out');
      resolve(false);
    });
  });
}

async function main() {
  console.log(`[PERMA-TUNNEL] Initializing permanent Localtunnel for ${EXPECTED_URL} via ${HOST}...`);

  while (true) {
    let tunnel = null;
    let healthInterval = null;
    let failedChecksCount = 0;

    try {
      console.log(`[PERMA-TUNNEL] Requesting tunnel at ${new Date().toISOString()}...`);
      tunnel = await localtunnel({
        port: PORT,
        subdomain: SUBDOMAIN,
        host: HOST
      });

      console.log(`[PERMA-TUNNEL] Granted URL: ${tunnel.url}`);

      if (tunnel.url !== EXPECTED_URL) {
        console.warn(`[PERMA-TUNNEL] Received ${tunnel.url} instead of ${EXPECTED_URL}. Waiting 3s to reclaim...`);
        try { tunnel.close(); } catch (_) {}
        await new Promise((r) => setTimeout(r, 3000));
        continue;
      }

      console.log(`[PERMA-TUNNEL] *** FIXED PERMANENT LINK IS LIVE ***: ${EXPECTED_URL}`);

      await new Promise((resolve) => {
        let isDone = false;
        const triggerReconnect = (reason) => {
          if (isDone) return;
          isDone = true;
          if (healthInterval) clearInterval(healthInterval);
          console.warn(`[PERMA-TUNNEL] Triggering reconnect: ${reason}`);
          resolve();
        };

        tunnel.on('close', () => triggerReconnect('tunnel close event'));
        tunnel.on('error', (err) => triggerReconnect(`socket error: ${err.message || err}`));

        // Active health checks with failure tolerance (2 consecutive failures)
        healthInterval = setInterval(async () => {
          if (isDone) return;
          const healthy = await checkTunnelHealth();
          if (healthy) {
            failedChecksCount = 0;
          } else {
            failedChecksCount++;
            console.warn(`[PERMA-TUNNEL] Health check failed count: ${failedChecksCount}/2`);
            if (failedChecksCount >= 2) {
              triggerReconnect('consecutive health checks failed');
            }
          }
        }, HEALTH_CHECK_INTERVAL_MS);
      });
    } catch (err) {
      console.error('[PERMA-TUNNEL] Setup error:', err.message || err);
    } finally {
      if (healthInterval) clearInterval(healthInterval);
      if (tunnel) {
        try { tunnel.close(); } catch (_) {}
      }
    }

    console.log('[PERMA-TUNNEL] Backing off 3s before auto-reconnect...');
    await new Promise((r) => setTimeout(r, 3000));
  }
}

main();
