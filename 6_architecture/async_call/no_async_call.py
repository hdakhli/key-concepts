import asyncio
import uvicorn
from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/get-a-joke")
def get_a_joke() -> list:

    dog_response = call_api('https://dog.ceo/api/breeds/image/random')
    user_response = call_api('https://randomuser.me/api/')
    joke_response = call_api('https://official-joke-api.appspot.com/random_joke')

    responses = [dog_response, joke_response, user_response]

    return responses


def call_api(url):
    response = requests.get(url)
    return response.json()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)

# responses = await asyncio.gather(dog_response, joke_response, user_response)
