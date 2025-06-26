from core.upload import upload_file
from core.tuning import create_fine_tune_job, wait_for_completion
from core.inference import ask_model


if __name__ == "__main__":
    file_path = "training_data/train.jsonl"

    file_id = upload_file(file_path)
    job_id = create_fine_tune_job(file_id)
    model_name = wait_for_completion(job_id)

    print("Trained model:", model_name)

    response = ask_model(model_name, "O que a empresa XPTO faz?")
    print("New Model Response:", response)
