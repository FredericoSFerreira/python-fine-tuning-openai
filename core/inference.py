import requests
from config.settings import HEADERS, BASE_URL

def ask_model(model, question):
    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": question}
        ]
    }
    response = requests.post(
        f"{BASE_URL}/v1/chat/completions",
        headers=HEADERS,
        json=payload
    )
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
