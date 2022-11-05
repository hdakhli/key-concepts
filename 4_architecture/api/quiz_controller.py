import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()


class Quiz(BaseModel):
    user_name: str
    question_id: int
    answer_id: int


@app.get("/say-hello")
def say_hello(user_name: str) -> str:
    print(f"{user_name} connecté!")
    return f"Hello {user_name}"


@app.post("/send-answer")
def answer(quiz: Quiz) -> bool:
    print(
        f"{quiz.user_name} a envoyé la réponse: {quiz.answer_id} "
        f"pour la question: {quiz.question_id}")
    return True


@app.get("/get-a-joke")
def get_a_joke(user_name: str) -> dict:
    dog_response = call_api('https://dog.ceo/api/breeds/image/random')
    user_response = call_api('https://randomuser.me/api/')
    joke_response = call_api(
        'https://official-joke-api.appspot.com/random_joke')
    print(f"{user_name} connecté!")
    return dict(joke_response, **user_response, **dog_response)


def call_api(url):
    response = requests.get(url)
    return response.json()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
