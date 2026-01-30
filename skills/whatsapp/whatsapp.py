import requests
import os

MAC_IP = os.getenv("MAC_TAILSCALE_IP", "localhost")
BASE_URL = f"http://{MAC_IP}:3002"

def send_text(to, message):
    """Send a text message to a phone number or JID."""
    try:
        resp = requests.post(f"{BASE_URL}/send/text", json={"to": to, "message": message}, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def send_file(to, file_path, caption=None):
    """Send a file (local path on the Mac) to a recipient."""
    payload = {"to": to, "file": file_path}
    if caption:
        payload["caption"] = caption
        
    try:
        resp = requests.post(f"{BASE_URL}/send/file", json=payload, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def list_messages(query=None, limit=10):
    """List or search messages."""
    params = {"limit": limit}
    if query:
        params["query"] = query
        
    try:
        resp = requests.get(f"{BASE_URL}/messages", params=params, timeout=10)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
