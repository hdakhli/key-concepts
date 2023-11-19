import random
from datetime import datetime

import requests
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/get-a-random")
def get_a_random_data() -> list:
    start = datetime.now()

    dog_response = call_api('https://dog.ceo/api/breeds/image/random')
    cat_response = call_api('https://catfact.ninja/fact')
    pokemon_response = call_api(f'https://pokeapi.co/api/v2/pokemon/{random.randint(0, 100)}')
    user_response = call_api('https://randomuser.me/api/')
    joke_response = call_api('https://official-joke-api.appspot.com/random_joke')
    products_response = call_api('https://hub.dummyapis.com/products?noofRecords=10&idStarts=1001&currency=usd')

    responses = [dog_response, cat_response, pokemon_response, joke_response, user_response, products_response]

    end = datetime.now()
    print(f"duration = {end - start}")

    return responses


def call_api(url):
    response = requests.get(url)
    return response.json()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
