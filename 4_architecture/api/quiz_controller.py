import asyncio
import time

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()


@app.get("/say-hello")
def say_hello(user_name: str) -> str:
    print(f"{user_name} connecté!")
    return f"Hello {user_name}"


class Quiz(BaseModel):
    user_name: str
    question_id: int
    answer_id: int


@app.post("/send-answer")
def answer(quiz: Quiz) -> bool:
    print(
        f"{quiz.user_name} a envoyé la réponse: {quiz.answer_id} "
        f"pour la question: {quiz.question_id}")
    return True


@app.get("/get-a-joke")
def get_a_joke(user_name: str) -> list:
    start_time = time.time()
    dog_response = call_api('https://dog.ceo/api/breeds/image/random')
    user_response = call_api('https://randomuser.me/api/')
    joke_response = call_api(
        'https://official-joke-api.appspot.com/random_joke')

    print(f"{user_name} connecté!")

    responses = [dog_response, joke_response, user_response]

    end_time = time.time()
    duration = end_time - start_time
    print(f"Duration: {duration}")

    return responses


def call_api(url):
    response = requests.get(url)
    return response.json()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)





# responses = await asyncio.gather(dog_response, joke_response, user_response)