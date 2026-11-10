
import json
import os

import httpx
from dotenv import load_dotenv

load_dotenv()

OLLAMA_URL = os.getenv(
    "OLLAMA_URL",
    "http://localhost:11434"
)

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "qwen2.5:3b"
)


def generate_json(prompt: str, schema: dict | None = None) -> dict:
    payload = {
        "model": OLLAMA_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
        "format": schema or "json",
        "options": {
            "temperature": 0,
            "num_ctx": 2048
        }
    }

    try:
        response = httpx.post(
            f"{OLLAMA_URL}/api/chat",
            json=payload,
            timeout=120.0
        )

        response.raise_for_status()

        result = response.json()
        content = result["message"]["content"]

        return json.loads(content)

    except httpx.HTTPError as exc:
        raise RuntimeError(
            f"Could not communicate with Ollama: {exc}"
        ) from exc

    except (KeyError, ValueError) as exc:
        raise RuntimeError(
            f"Invalid response received from Ollama: {exc}"
        ) from exc
