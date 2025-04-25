from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from fastapi import Request


app = FastAPI()

@app.get("/")
async def root():
    return{"message": "Hello World"}

@app.get("/greet/{name}")
async def greet_name(name: str) -> dict:
    return {"message": f"Hello {name}"}


@app.get("/greet")
async def greet_default_name(name:Optional[str] = "User", age: int = 0) -> dict:
    return {"message": f"Hello {name}, age: {age}"}


class BookCreateModel(BaseModel):
    title: str
    author: str

@app.post("/create_book")
async def create_book(book_data:BookCreateModel):
    return {
        "title": book_data.title,
        "author": book_data.author
    }


@app.get("/check")
async def check_headers(request: Request):
    headers = request.headers
    user_agent = headers.get("user-agent")
    return {"user-agent": user_agent}