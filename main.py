import json

from fastapi import FastAPI

from schemas import QuizInput
from groq_client import review_test

app = FastAPI()


@app.post("/")
def submit(data: QuizInput):
    message = data.model_dump_json()
    response = review_test(message)

    return response
