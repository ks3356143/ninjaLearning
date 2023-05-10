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

# 下面是展示用户的数据
class queryInfoSchema(Schema):
    offset:int = 0
    size:int = 10

@api.post("/user/list")
def user_lists(request, data:queryInfoSchema):
    print(data)
    result = {
        "code": 0,
        "data": {
            "list": [
                {
                    "id": 45,
                    "name": "james",
                    "realname": "詹姆斯",
                    "cellphone": 13322223338,
                    "enable": 1,
                    "department": 1,
                    "roleId": 1,
                    "createAt": "2021-08-08T02:59:13.000Z",
                    "updateAt": "2021-08-08T02:59:13.000Z"
                },
                {
                    "id": 42,
                    "name": "jerry",
                    "realname": "杰瑞",
                    "cellphone": 13800000000,
                    "enable": 1,
                    "department": 1,
                    "roleId": 1,
                    "createAt": "2021-08-07T06:59:13.000Z",
                    "updateAt": "2021-08-07T06:59:13.000Z"
                },
                {
                    "id": 9,
                    "name": "lwx",
                    "realname": "林伟翔",
                    "cellphone": 13625412489,
                    "enable": 1,
                    "department": 1,
                    "roleId": 1,
                    "createAt": "2021-09-08T12:59:13.000Z",
                    "updateAt": "2021-09-08T12:59:13.000Z"
                },
                {
                    "id": 12,
                    "name": "james2",
                    "realname": "詹姆斯二号",
                    "cellphone": 13322223338,
                    "enable": 1,
                    "department": 1,
                    "roleId": 1,
                    "createAt": "2022-08-08T02:59:13.000Z",
                    "updateAt": "2022-08-08T02:59:13.000Z"
                },
                {
                    "id": 1,
                    "name": "chen",
                    "realname": "陈俊亦",
                    "cellphone": 18782947123,
                    "enable": 1,
                    "department": 1,
                    "roleId": 1,
                    "createAt": "2023-01-08T02:59:13.000Z",
                    "updateAt": "2023-01-08T02:59:13.000Z"
                },
            ],
            "totalCount":5
        }
    }
    return result
