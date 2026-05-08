import requests

SERVER_URL = "http://localhost:8000/upload"

pdf_path = "../documents/sample.pdf"

with open(pdf_path, "rb") as file:

    response = requests.post(
        SERVER_URL,
        files={"file": file}
    )

print(response.json())