import json
from typing import Union
from fastapi import FastAPI, Request
import utils.user_request_models as user_request_models
import utils.generator_utils as generator
from bbd import worker
import os

app = FastAPI()

# 카카오 챗봇의 기본 METHOD는 HTTP POST
# 사용자 발화 반환
@app.post("/utterance")
async def process_utterance(request: Request):
    payload = await request.json()
    request_payload = user_request_models.RequestPayload(**payload)
    utterance = request_payload.userRequest.utterance
    user_id = request_payload.userRequest.user.id

    task = "record"
    user_request = {
        "user_id": user_id,
        "user_text": utterance
    }
    bbd_worker = worker(task, **user_request)
    user_path = "/home/ec2-user/user_files"
    with open(os.path.join(user_path, "user_info.json"), "w") as f:
        user_json = json.load(f)
    user_json[user_id]["api_key"] = os.path.join(user_path, user_json[user_id]["api_key"])

    output = bbd_worker(user_json)

    if output.trial:
        response_string  = "등록 완료되었습니다. 버버두두!"
    else:
        response_string = "등록 실패했습니다. 버버두두!"
    
    # json 형식의 응답 생성
    return generator.generate_chat(response_string)

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