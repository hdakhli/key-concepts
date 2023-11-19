import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/say-hello")
def say_hello(username: str) -> dict:
    print(f"{username} connecté!")
    return {
        "greeting": "Hello!",
        "username": username
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
