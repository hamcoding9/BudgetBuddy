# str을 받아서 카카오톡 채팅 json 형식을 만들어 내는 함수
def generate_chat(message: str) -> dict:
    result = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": message
                    }
                }
            ]
        }
    }
    return result