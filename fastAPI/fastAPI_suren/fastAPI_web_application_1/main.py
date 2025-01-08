from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
import uvicorn

app = FastAPI()

# EmailStr - валидатор по почте, есть в pydantic, устанавливается через: pip install "pydantic[email]"
# EmailStr - сторонняя библиотека, которая позволяет проверять emails
# чтобы принимать email именно в Body, а не в строке запроса: def create_user(email: EmailStr = Body()):
# Но мы хотим принимать Email в виде строчки в Body, а в виде объекта json, вместе с другими параметрами, 
# которые через Body пойдут в json объект - решение: использование pydantic-объектов - из 
# pydantic импортировать BaseModel - базовая модель
class CreateUser(BaseModel):
    email: EmailStr


@app.get("/")
def hello_index():
    return {"message": "Hello index"}

@app.get("/hello/")
def hello(name: str = "World"):
    name = name.strip().title()
    return {"message": f"Hello, {name}!"}

# email надо передавать в Body, иначе ничем не отличается от запроса /hello/
# для этого создали класс CreateUser, который наследуется от BaseModel библиотеки pydantic
@app.post("/users/")
def create_user(user: CreateUser):
    return {
        "message": "success",
        "email": user.email,
    }

@app.post("/calc/add/")
def add(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "result": a + b,
    }

@app.get("/items/")
def list_items():
    return [
        "Item1",
        "Item2",
    ]
# 1) order is important
@app.get("/items/latest/")
def get_latest_item():
    return {"items": {"id": "0", "name": "latest"}}

# 2) order is important
@app.get("/items/{item_id}/")
def get_item_by_id(item_id: int):
    return {
        "item": {
            "id": item_id,
        }
    }


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)