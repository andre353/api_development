from fastapi import FastAPI
from typing import Optional

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
@app.get("/greet")
async def greet_name(name: Optional[str] = "User") -> dict:
    return {"message": f"Hello {name}"}


# if __name__ == "__main__":
#     uvicorn.run("main:app", reload=True)
# uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, log_level="debug", debug=True,
#             workers=1, limit_concurrency=1, limit_max_requests=1)
