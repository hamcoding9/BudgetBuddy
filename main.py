from typing import Union
from fastapi import FastAPI, Request
import user_request_models
import random

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

# 랜덤 문자열 선택 함수
def get_random_string():
    strings = [
        "영아기", "유아기", "초등학생", "중학생", 
        "고등학생", "대학생", "석사생", "박사생", 
        "사원", "대리", "과장"
    ]
    return random.choice(strings)

# 기본 문자열 반환 함수 테스트
@app.post("/random")
def random_():
    # 랜덤 문자열 선택
    random_string = "당신의 지출 관리 레벨은 " + get_random_string() + "입니다."
    
    # JSON 형식의 응답 생성
    response_data = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": random_string
                    }
                }
            ]
        }
    }
    
    # JSON 응답 반환
    return response_data

# 지출 카테고리 반환
@app.post("/category")
def category():
    # JSON 형식의 응답 생성
    response_data = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "지출 카테고리는 다음과 같습니다."
                    },
                        "quickReplies": [
                    {
                        "messageText": "영적",
                        "action": "message",
                        "label": "영적"
                    },
                    {
                        "messageText": "지적",
                        "action": "message",
                        "label": "지적"
                    },
                    {
                        "messageText": "신체적",
                        "action": "message",
                        "label": "신체적"
                    },
                    {
                        "messageText": "사회적",
                        "action": "message",
                        "label": "사회적"
                    },
                    {
                        "messageText": "낭비",
                        "action": "message",
                        "label": "낭비"
                    }
                    ]
                }
            ]
        }
    }
    
    # JSON 응답 반환
    return response_data

# 사용자 발화 반환
@app.post("/utterance")
async def process_utterance(request: Request):
    # 사용자 입력 json에서 사용자 발화 받아오기
    # 나중에 util 함수로 빼면 될듯
    payload = await request.json()
    request_payload = user_request_models.RequestPayload(**payload)
    utterance = request_payload.userRequest.utterance

    # json 형식의 응답 생성
    response_string = utterance + "\n등록 완료되었습니다. 버버두두!"
    response_data = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": response_string
                    }
                }
            ]
        }
    }
    return response_data