import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'shine', 'okx'))
from okx_client import OKXClient

c = OKXClient(os.path.join('shine', 'okx', 'config.json'))
r = c.get_positions()
print("=== Current Positions ===")
if r.get('data'):
    for p in r['data']:
        if float(p.get('pos', 0)) != 0:
            print(f"  {p['instId']}: pos={p['pos']} avgPx={p['avgPx']} upl={p['upl']}")

# Check pending algo orders for RAVE
print("\n=== RAVE Algo Orders ===")
for ot in ['conditional', 'oco', 'trigger']:
    ar = c._request("GET", "/api/v5/trade/orders-algo-pending", params={"instId": "RAVE-USDT-SWAP", "ordType": ot})
    if ar.get('data'):
        for a in ar['data']:
            print(f"  type={ot} slPx={a.get('slTriggerPx','')} tpPx={a.get('tpTriggerPx','')} state={a.get('state','')}")

# Check algo history
print("\n=== RAVE Algo History (filled) ===")
ah = c._request("GET", "/api/v5/trade/orders-algo-history", params={"instId": "RAVE-USDT-SWAP", "ordType": "conditional", "state": "effective"})
if ah.get('data'):
    for a in ah['data']:
        print(f"  sl={a.get('slTriggerPx','')} tp={a.get('tpTriggerPx','')} state={a.get('state','')} triggered={a.get('triggerTime','')}")
else:
    print("  (none)")
