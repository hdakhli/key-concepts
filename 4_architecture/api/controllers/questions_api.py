import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Answer(BaseModel):
    user_name: str
    question: int
    answer: int


@app.get("/say-hello")
def say_hello(user_name: str) -> str:
    print(f"{user_name} connecté!")
    return f"Hello {user_name}"


@app.post("/send-answer")
def answer(answer: Answer) -> bool:
    print(
        f"{answer.user_name} a envoyé la réponse: {answer.answer} "
        f"for question: {answer.question}")
    return True


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
