const localtunnel = require('localtunnel');
const http = require('http');

const PORT = 8080;
const SUBDOMAIN = 'officerpass-vashishta';
const HOST = 'https://loca.lt';
const EXPECTED_URL = `https://${SUBDOMAIN}.loca.lt`;

async function main() {
  console.log(`[PERMA-TUNNEL] Initializing permanent Localtunnel for ${EXPECTED_URL} via ${HOST}...`);
  
  while (true) {
    let tunnel = null;
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
        tunnel.close();
        await new Promise(r => setTimeout(r, 3000));
        continue;
      }
      
      console.log(`[PERMA-TUNNEL] *** FIXED PERMANENT LINK IS LIVE ***: ${EXPECTED_URL}`);
      
      await new Promise(resolve => {
        tunnel.on('close', () => {
          console.warn('[PERMA-TUNNEL] Tunnel closed. Reconnecting...');
          resolve();
        });
        
        tunnel.on('error', err => {
          console.warn('[PERMA-TUNNEL] Handled socket error:', err.message);
          resolve();
        });
      });
    } catch (err) {
      console.error('[PERMA-TUNNEL] Setup error:', err.message);
    }
    
    if (tunnel) {
      try { tunnel.close(); } catch (_) {}
    }
    
    console.log('[PERMA-TUNNEL] Backing off 3s before auto-reconnect...');
    await new Promise(r => setTimeout(r, 3000));
  }
}

main();
