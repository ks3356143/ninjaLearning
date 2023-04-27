from ninja import NinjaAPI, Schema
import jwt

api = NinjaAPI()

class LoginSchema(Schema):
    name: str
    password: str

@api.post("/login")
def login(request, data: LoginSchema):
    result = {"code": 0, "data": {"id": 0, "name": "", "token": ""}}
    name = data.name
    password = data.password
    b = {'name': name, 'password': password}
    token = jwt.encode(b, 'secret', algorithm='HS256')
    result["data"]["name"] = name
    result["data"]["token"] = token
    return result

@api.get("/users/{user_id}")
def userInfo(request, user_id: int):
    result = {"code": 0, "data": {"id": 0, "name": ""}}
    result["data"]["name"] = "陈俊亦"
    return result
