import requests
import os

MAC_IP = os.getenv("MAC_TAILSCALE_IP", "localhost")
BASE_URL = f"http://{MAC_IP}:3003"

def run_applescript(script):
    """Execute raw AppleScript code."""
    try:
        resp = requests.post(f"{BASE_URL}/applescript", json={"script": script}, timeout=60)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def run_jxa(code):
    """Execute JavaScript for Automation (JXA) code."""
    try:
        resp = requests.post(f"{BASE_URL}/jxa", json={"code": code}, timeout=60)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
