import requests

SERVER_URL = "http://localhost:8000/upload"

#pdf_path = "../documents/python_book_01.pdf"
pdf_path = r"D:\courses\data science\presentation\nlp\course 26-27\agentic-workflow\documents\python_book_01.pdf"
with open(pdf_path, "rb") as file:

    response = requests.post(
        SERVER_URL,
        files={"file": file}
    )

print(response.json())


