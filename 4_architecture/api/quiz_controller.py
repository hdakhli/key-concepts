import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

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


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
