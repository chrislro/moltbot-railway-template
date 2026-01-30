import requests
import os

# Config - configured via Env Vars in Railway
MAC_IP = os.getenv("MAC_TAILSCALE_IP", "localhost") # Default to localhost for testing
BASE_URL = f"http://{MAC_IP}:3001"

def run(args):
    """Run a raw peekaboo command.
    Args:
        args (list): List of command line arguments, e.g. ["see", "--json"]
    """
    try:
        resp = requests.post(f"{BASE_URL}/run", json={"args": args}, timeout=30)
        resp.raise_for_status()
        return resp.json()
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
