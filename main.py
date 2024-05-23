from typing import Union
from fastapi import FastAPI, Request
import user_request_models
import random

app = FastAPI()

# 카카오 챗봇의 기본 METHOD는 HTTP POST
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

# 사용자 id 반환
@app.post("/user")
async def process_utterance(request: Request):
    # 사용자 입력 json에서 사용자 id 받아오기
    # 나중에 util 함수로 빼면 될듯
    payload = await request.json()
    request_payload = user_request_models.RequestPayload(**payload)
    user_id = request_payload.userRequest.user.id

    # json 형식의 응답 생성
    response_string = "사용자 아이디는 " + user_id + " 입니다."
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