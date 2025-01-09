from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

# import uvicorn

app = FastAPI()


@app.get("/")
async def index():
    return {"messsage": "Hello World"}


# /greet/John - path parameter
# @app.get('/greet/{name}')
# async def greet_name(name: str) -> dict:
#     return {"message": f"Hello {name}"}


# /greet?name=John - query parameter
# /greet?name=John&age=31 - query parameters
@app.get("/greet")
async def greet_name(name: Optional[str] = "User", age: int = 0) -> dict:
    return {"message": f"Hello {name}, your age is {age}"}


# a Pydantic model with serialization to JSON format
class BookCreateModel(BaseModel):
    title: str
    author: str


@app.post("/create_book")
async def create_book(book_data: BookCreateModel):
    return {"title": book_data.title, "author": book_data.author}


# if __name__ == "__main__":
#     uvicorn.run("main:app", reload=True)
# uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, log_level="debug", debug=True,
#             workers=1, limit_concurrency=1, limit_max_requests=1)
