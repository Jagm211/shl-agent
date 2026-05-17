from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: List[Message]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat")
def chat(req: ChatRequest):

    last_message = req.messages[-1].content.lower()

    if "assessment" in last_message and len(last_message.split()) < 4:
        return {
            "reply": "Which role are you hiring for and what seniority level?",
            "recommendations": [],
            "end_of_conversation": False
        }

    recommendations = [
        {
            "name": "OPQ32r",
            "url": "https://www.shl.com/solutions/products/product-catalog/",
            "test_type": "P"
        },
        {
            "name": "Java 8 (New)",
            "url": "https://www.shl.com/solutions/products/product-catalog/",
            "test_type": "K"
        }
    ]

    return {
        "reply": "Here are recommended SHL assessments.",
        "recommendations": recommendations,
        "end_of_conversation": False
    }