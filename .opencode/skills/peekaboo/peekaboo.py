import urllib.request
import json
import os

# Config - configured via Env Vars in Railway
MAC_IP = os.getenv("MAC_TAILSCALE_IP", "localhost")
BASE_URL = f"http://{MAC_IP}:3001"

def run(args):
    """Run a raw peekaboo command."""
    url = f"{BASE_URL}/run"
    data = json.dumps({"args": args}).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except Exception as e:
        return {"error": str(e)}

def see():
    """Capture screen and detect elements. Returns JSON with element tree."""
    return run(["see", "--mode", "screen", "--json"])

def click(element_id):
    """Click an element by ID (e.g., "A1" from a previous see() call)"""
    return run(["click", "--on", element_id])

def type_text(text):
    """Type text into the focused element"""
    return run(["type", text])
