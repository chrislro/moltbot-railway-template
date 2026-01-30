import urllib.request
import json
import os

MAC_IP = os.getenv("MAC_TAILSCALE_IP", "localhost")
BASE_URL = f"http://{MAC_IP}:3002"

def _post(endpoint, payload):
    url = f"{BASE_URL}{endpoint}"
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except Exception as e:
        return {"error": str(e)}

def send_text(to, message):
    return _post("/send/text", {"to": to, "message": message})

def send_file(to, file_path, caption=None):
    payload = {"to": to, "file": file_path}
    if caption:
        payload["caption"] = caption
    return _post("/send/file", payload)

def list_messages(query=None, limit=10):
    params = urllib.parse.urlencode({"limit": limit, "query": query or ""})
    url = f"{BASE_URL}/messages?{params}"
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            return json.loads(response.read().decode("utf-8"))
    except Exception as e:
        return {"error": str(e)}
