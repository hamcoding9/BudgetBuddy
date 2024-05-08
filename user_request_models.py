from pydantic import BaseModel

class UserRequest(BaseModel):
    timezone: str
    params: dict
    block: dict
    utterance: str
    lang: str
    user: dict

class Action(BaseModel):
    name: str

class RequestPayload(BaseModel):
    userRequest: UserRequest
    action: Action