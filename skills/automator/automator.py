import urllib.request
import json
import os

MAC_IP = os.getenv("MAC_TAILSCALE_IP", "localhost")
BASE_URL = f"http://{MAC_IP}:3003"

def _post(endpoint, payload):
    url = f"{BASE_URL}{endpoint}"
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as response:
            return json.loads(response.read().decode("utf-8"))
    except Exception as e:
        return {"error": str(e)}

def run_applescript(script):
    return _post("/applescript", {"script": script})

def run_jxa(code):
    return _post("/jxa", {"code": code})
