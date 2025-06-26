import requests
from config.settings import BASE_URL, HEADERS

def upload_file(file_path):
    print("Enviando arquivo para fine-tuning...")
    with open(file_path, 'rb') as f:
        print(HEADERS)
        response = requests.post(
            f"{BASE_URL}/v1/files",
            headers={**HEADERS, "Content-Type": None},
            files={"file": f},
            data={"purpose": "fine-tune"}
        )
    response.raise_for_status()
    file_id = response.json()["id"]
    print(f"Arquivo enviado com sucesso. ID: {file_id}")
    return file_id