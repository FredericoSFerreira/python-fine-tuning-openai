import requests
import time
from config.settings import BASE_URL, MODEL, HEADERS

def create_fine_tune_job(file_id):
    response = requests.post(
        f"{BASE_URL}/v1/fine_tuning/jobs",
        headers=HEADERS,
        json={"training_file": file_id, "model": MODEL}
    )
    response.raise_for_status()
    job = response.json()
    print(f"Job criado. ID: {job['id']}")
    return job["id"]

def wait_for_completion(job_id):
    print("Aguardando o fine-tuning ser concluído...")
    status = "running"
    model_name = None
    while status in ["running", "validating_files", "queued"]:
        time.sleep(10)
        res = requests.get(
            f"{BASE_URL}/v1/fine_tuning/jobs/{job_id}",
            headers=HEADERS
        )
        res.raise_for_status()
        data = res.json()
        status = data["status"]
        model_name = data.get("fine_tuned_model")
        print(f"Status atual: {status}")
    print("Fine-tuning finalizado!")
    print(f"Modelo treinado: {model_name}")
    return model_name
