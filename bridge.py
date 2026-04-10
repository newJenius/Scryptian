# bridge.py — Bridge between Scryptian plugins and Ollama
# Connector | Optimizer | Unifier

import requests
import json

# ── Connection settings ──
OLLAMA_HOST = "http://localhost"
OLLAMA_PORT = 11434
OLLAMA_URL = f"{OLLAMA_HOST}:{OLLAMA_PORT}/api/generate"

# ── Model settings ──
MODEL = "phi3:mini"
TEMPERATURE = 0
KEEP_ALIVE = "30m"


def generate(prompt: str) -> str:
    """
    Single LLM entry point for all plugins.
    Takes a prompt (string), returns model response (string).
    """
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "temperature": TEMPERATURE,
        "keep_alive": KEEP_ALIVE,
        "stream": False,
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=120)
        response.raise_for_status()
        data = response.json()
        return data.get("response", "").strip()
    except requests.ConnectionError:
        return "[Scryptian Error] Could not connect to Ollama. Make sure the server is running."
    except requests.Timeout:
        return "[Scryptian Error] Ollama did not respond in time (timeout 120s)."
    except Exception as e:
        return f"[Scryptian Error] {e}"
