from pydantic import BaseModel

class Action(BaseModel):
    name: str
    
class User(BaseModel):
    id: str
    type: str
    properties: dict

class UserRequest(BaseModel):
    timezone: str
    params: dict
    block: dict
    utterance: str
    lang: str
    user: User

class RequestPayload(BaseModel):
    userRequest: UserRequest
    action: Action