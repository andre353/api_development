from fastapi import FastAPI
# import uvicorn

app = FastAPI()

@app.get('/')
async def index():
    return {"messsage":"Hello World"}

@app.get('/greet/{name}')    
async def greet_name(name: str) -> dict:
    return {"message": f"Hello {name}"}

# if __name__ == "__main__":
#     uvicorn.run("main:app", reload=True)
    # uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, log_level="debug", debug=True,
    #             workers=1, limit_concurrency=1, limit_max_requests=1)