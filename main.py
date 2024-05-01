from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root() -> Union[str, dict]:
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None) -> dict:
    return {"item_id": item_id, "q": q}

# 카카오 챗봇의 기본 METHOD는 HTTP POST
@app.post("/hello")
def hello_world():
    return {"Hello": "World"}
