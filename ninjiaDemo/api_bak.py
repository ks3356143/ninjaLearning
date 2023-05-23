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
    offset: int = 0
    size: int = 10

@api.post("/user/list")
def user_lists(request, data: queryInfoSchema):
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
                    "enable": 0,
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
            "totalCount": 5
        }
    }
    return result

@api.post("/role/list")
def role_list(request, data: queryInfoSchema):
    result = {
        "code": 0,
        "data": {
            "list": [
                {
                    "id": 1,
                    "name": "james",
                    "introduce": "詹姆斯",
                    "createAt": "2021-08-08T02:59:13.000Z",
                },
                {
                    "id": 2,
                    "name": "jerry",
                    "introduce": "杰瑞",
                    "createAt": "2021-08-07T06:59:13.000Z",
                },
                {
                    "id": 3,
                    "name": "lwx",
                    "introduce": "林伟翔",
                    "createAt": "2021-09-08T12:59:13.000Z",
                },
            ],
            "totalCount": 5
        }
    }
    return result

@api.post("/goods/list")
def role_list(request, data: queryInfoSchema):
    print(data)
    offset = data.offset
    size = data.size
    result = {
        "code": 0,
        "data": {
            "list": [
                {
                    "id": 7,
                    "name": "wuaduowihdaowd",
                    "oldPrice": "127",
                    "newPrice": "89",
                    "desc": "wuaduowihdaowd",
                    "status": 1,
                    "imgUrl": "http://s3.mogucdn.com/mlcdn/c45406/180828_550k23i82cbibh32602fl43jc9aid_800x1200.jpg_560x999.jpg",
                    "inventoryCount": 4044,
                    "saleCount": 32070,
                    "favorCount": 179,
                    "address": "上海",
                    "categoryId": 7,
                    "createAt": "2021-08-08T02:59:13.000Z",
                    "updateAt": "2022-04-09T08:09:55.000Z"
                },
                {
                    "id": 8,
                    "name": "秋装女2018新款早秋女装裙子针织连衣裙套装",
                    "oldPrice": "127",
                    "newPrice": "89",
                    "desc": "秋装女2018新款早秋女装裙子针织连衣裙套装",
                    "status": 1,
                    "imgUrl": "http://s3.mogucdn.com/mlcdn/c45406/180828_550k23i82cbibh32602fl43jc9aid_800x1200.jpg_560x999.jpg",
                    "inventoryCount": 4044,
                    "saleCount": 32070,
                    "favorCount": 179,
                    "address": "上海",
                    "categoryId": 7,
                    "createAt": "2021-08-08T02:59:13.000Z",
                    "updateAt": "2022-04-09T08:09:55.000Z"
                },
                {
                    "id": 9,
                    "name": "秋装女2018新款早秋女装裙子针织连衣裙套装",
                    "oldPrice": "127",
                    "newPrice": "89",
                    "desc": "秋装女2018新款早秋女装裙子针织连衣裙套装",
                    "status": 1,
                    "imgUrl": "http://s3.mogucdn.com/mlcdn/c45406/180828_550k23i82cbibh32602fl43jc9aid_800x1200.jpg_560x999.jpg",
                    "inventoryCount": 4044,
                    "saleCount": 32070,
                    "favorCount": 179,
                    "address": "上海",
                    "categoryId": 7,
                    "createAt": "2021-08-08T02:59:13.000Z",
                    "updateAt": "2022-04-09T08:09:55.000Z"
                },
                {
                    "id": 10,
                    "name": "秋装女2018新款早秋女装裙子针织连衣裙套装",
                    "oldPrice": "127",
                    "newPrice": "89",
                    "desc": "秋装女2018新款早秋女装裙子针织连衣裙套装",
                    "status": 1,
                    "imgUrl": "http://s3.mogucdn.com/mlcdn/c45406/180828_550k23i82cbibh32602fl43jc9aid_800x1200.jpg_560x999.jpg",
                    "inventoryCount": 4044,
                    "saleCount": 32070,
                    "favorCount": 179,
                    "address": "上海",
                    "categoryId": 7,
                    "createAt": "2021-08-08T02:59:13.000Z",
                    "updateAt": "2022-04-09T08:09:55.000Z"
                },
                {
                    "id": 11,
                    "name": "秋装女2018新款早秋女装裙子针织连衣裙套装",
                    "oldPrice": "127",
                    "newPrice": "89",
                    "desc": "秋装女2018新款早秋女装裙子针织连衣裙套装",
                    "status": 1,
                    "imgUrl": "http://s3.mogucdn.com/mlcdn/c45406/180828_550k23i82cbibh32602fl43jc9aid_800x1200.jpg_560x999.jpg",
                    "inventoryCount": 4044,
                    "saleCount": 32070,
                    "favorCount": 179,
                    "address": "上海",
                    "categoryId": 7,
                    "createAt": "2021-08-08T02:59:13.000Z",
                    "updateAt": "2022-04-09T08:09:55.000Z"
                },
                {
                    "id": 71,
                    "name": "秋装女2018新款早秋女装裙子针织连衣裙套装",
                    "oldPrice": "127",
                    "newPrice": "89",
                    "desc": "秋装女2018新款早秋女装裙子针织连衣裙套装",
                    "status": 1,
                    "imgUrl": "http://s3.mogucdn.com/mlcdn/c45406/180828_550k23i82cbibh32602fl43jc9aid_800x1200.jpg_560x999.jpg",
                    "inventoryCount": 4044,
                    "saleCount": 32070,
                    "favorCount": 179,
                    "address": "上海",
                    "categoryId": 7,
                    "createAt": "2021-08-08T02:59:13.000Z",
                    "updateAt": "2022-04-09T08:09:55.000Z"
                },
                {
                    "id": 13,
                    "name": "秋装女2018新款早秋女装裙子针织连衣裙套装",
                    "oldPrice": "127",
                    "newPrice": "89",
                    "desc": "秋装女2018新款早秋女装裙子针织连衣裙套装",
                    "status": 1,
                    "imgUrl": "http://s3.mogucdn.com/mlcdn/c45406/180828_550k23i82cbibh32602fl43jc9aid_800x1200.jpg_560x999.jpg",
                    "inventoryCount": 4044,
                    "saleCount": 32070,
                    "favorCount": 179,
                    "address": "上海",
                    "categoryId": 7,
                    "createAt": "2021-08-08T02:59:13.000Z",
                    "updateAt": "2022-04-09T08:09:55.000Z"
                },
                {
                    "id": 14,
                    "name": "秋装女2018新款早秋女装裙子针织连衣裙套装",
                    "oldPrice": "127",
                    "newPrice": "89",
                    "desc": "秋装女2018新款早秋女装裙子针织连衣裙套装",
                    "status": 1,
                    "imgUrl": "http://s3.mogucdn.com/mlcdn/c45406/180828_550k23i82cbibh32602fl43jc9aid_800x1200.jpg_560x999.jpg",
                    "inventoryCount": 4044,
                    "saleCount": 32070,
                    "favorCount": 179,
                    "address": "上海",
                    "categoryId": 7,
                    "createAt": "2021-08-08T02:59:13.000Z",
                    "updateAt": "2022-04-09T08:09:55.000Z"
                },
                {
                    "id": 15,
                    "name": "秋装女2018新款早秋女装裙子针织连衣裙套装",
                    "oldPrice": "127",
                    "newPrice": "89",
                    "desc": "秋装女2018新款早秋女装裙子针织连衣裙套装",
                    "status": 1,
                    "imgUrl": "http://s3.mogucdn.com/mlcdn/c45406/180828_550k23i82cbibh32602fl43jc9aid_800x1200.jpg_560x999.jpg",
                    "inventoryCount": 4044,
                    "saleCount": 32070,
                    "favorCount": 179,
                    "address": "上海",
                    "categoryId": 7,
                    "createAt": "2021-08-08T02:59:13.000Z",
                    "updateAt": "2022-04-09T08:09:55.000Z"
                },
                {
                    "id": 16,
                    "name": "秋装女2018新款早秋女装裙子针织连衣裙套装",
                    "oldPrice": "127",
                    "newPrice": "89",
                    "desc": "秋装女2018新款早秋女装裙子针织连衣裙套装",
                    "status": 1,
                    "imgUrl": "http://s3.mogucdn.com/mlcdn/c45406/180828_550k23i82cbibh32602fl43jc9aid_800x1200.jpg_560x999.jpg",
                    "inventoryCount": 4044,
                    "saleCount": 32070,
                    "favorCount": 179,
                    "address": "上海",
                    "categoryId": 7,
                    "createAt": "2021-08-08T02:59:13.000Z",
                    "updateAt": "2022-04-09T08:09:55.000Z"
                },
                {
                    "id": 17,
                    "name": "秋装女2018新款早秋女装裙子针织连衣裙套装",
                    "oldPrice": "127",
                    "newPrice": "89",
                    "desc": "秋装女2018新款早秋女装裙子针织连衣裙套装",
                    "status": 1,
                    "imgUrl": "http://s3.mogucdn.com/mlcdn/c45406/180828_550k23i82cbibh32602fl43jc9aid_800x1200.jpg_560x999.jpg",
                    "inventoryCount": 4044,
                    "saleCount": 32070,
                    "favorCount": 179,
                    "address": "上海",
                    "categoryId": 7,
                    "createAt": "2021-08-08T02:59:13.000Z",
                    "updateAt": "2022-04-09T08:09:55.000Z"
                },
                {
                    "id": 18,
                    "name": "秋装女2018新款早秋女装裙子针织连衣裙套装",
                    "oldPrice": "127",
                    "newPrice": "89",
                    "desc": "秋装女2018新款早秋女装裙子针织连衣裙套装",
                    "status": 1,
                    "imgUrl": "http://s3.mogucdn.com/mlcdn/c45406/180828_550k23i82cbibh32602fl43jc9aid_800x1200.jpg_560x999.jpg",
                    "inventoryCount": 4044,
                    "saleCount": 32070,
                    "favorCount": 179,
                    "address": "上海",
                    "categoryId": 7,
                    "createAt": "2021-08-08T02:59:13.000Z",
                    "updateAt": "2022-04-09T08:09:55.000Z"
                },
                {
                    "id": 19,
                    "name": "秋装女2018新款早秋女装裙子针织连衣裙套装",
                    "oldPrice": "127",
                    "newPrice": "89",
                    "desc": "秋装女2018新款早秋女装裙子针织连衣裙套装",
                    "status": 1,
                    "imgUrl": "http://s3.mogucdn.com/mlcdn/c45406/180828_550k23i82cbibh32602fl43jc9aid_800x1200.jpg_560x999.jpg",
                    "inventoryCount": 4044,
                    "saleCount": 32070,
                    "favorCount": 179,
                    "address": "上海",
                    "categoryId": 7,
                    "createAt": "2021-08-08T02:59:13.000Z",
                    "updateAt": "2022-04-09T08:09:55.000Z"
                },
                {
                    "id": 20,
                    "name": "秋装女2018新款早秋女装裙子针织连衣裙套装",
                    "oldPrice": "127",
                    "newPrice": "89",
                    "desc": "秋装女2018新款早秋女装裙子针织连衣裙套装",
                    "status": 1,
                    "imgUrl": "http://s3.mogucdn.com/mlcdn/c45406/180828_550k23i82cbibh32602fl43jc9aid_800x1200.jpg_560x999.jpg",
                    "inventoryCount": 4044,
                    "saleCount": 32070,
                    "favorCount": 179,
                    "address": "上海",
                    "categoryId": 7,
                    "createAt": "2021-08-08T02:59:13.000Z",
                    "updateAt": "2022-04-09T08:09:55.000Z"
                },
                {
                    "id": 21,
                    "name": "秋装女2018新款早秋女装裙子针织连衣裙套装",
                    "oldPrice": "127",
                    "newPrice": "89",
                    "desc": "秋装女2018新款早秋女装裙子针织连衣裙套装",
                    "status": 1,
                    "imgUrl": "http://s3.mogucdn.com/mlcdn/c45406/180828_550k23i82cbibh32602fl43jc9aid_800x1200.jpg_560x999.jpg",
                    "inventoryCount": 4044,
                    "saleCount": 32070,
                    "favorCount": 179,
                    "address": "上海",
                    "categoryId": 7,
                    "createAt": "2021-08-08T02:59:13.000Z",
                    "updateAt": "2022-04-09T08:09:55.000Z"
                },
                {
                    "id": 22,
                    "name": "秋装女2018新款早秋女装裙子针织连衣裙套装",
                    "oldPrice": "127",
                    "newPrice": "89",
                    "desc": "秋装女2018新款早秋女装裙子针织连衣裙套装",
                    "status": 1,
                    "imgUrl": "http://s3.mogucdn.com/mlcdn/c45406/180828_550k23i82cbibh32602fl43jc9aid_800x1200.jpg_560x999.jpg",
                    "inventoryCount": 4044,
                    "saleCount": 32070,
                    "favorCount": 179,
                    "address": "上海",
                    "categoryId": 7,
                    "createAt": "2021-08-08T02:59:13.000Z",
                    "updateAt": "2022-04-09T08:09:55.000Z"
                },
            ],
            "totalCount": 16
        }
    }
    result["data"]["list"] = result["data"]["list"][offset:offset + size]
    return result

@api.post("/menu/list")
def role_list(request, data: queryInfoSchema):
    result = {
        "code": 0,
        "data": {
            "list": [
                {
                    "id": 38,
                    "name": "系统总览",
                    "type": 1,
                    "url": "/main/analysis",
                    "icon": "el-icon-monitor",
                    "sort": 1,
                    "createAt": "2021-08-08T02:59:13.000Z",
                    "updateAt": "2021-08-08T02:59:13.000Z",
                    "children": [
                        {
                            "id": 39,
                            "name": "ok1",
                            "type": 2,
                            "url": "/main/ok1",
                            "icon": "el-icon-monitor",
                            "sort": 2,
                            "createAt": "2021-08-08T02:59:13.000Z",
                            "updateAt": "2021-08-08T02:59:13.000Z",
                            "children": [{
                                "id": 40,
                                "name": "ok1-1",
                                "type": 3,
                                "url": "/main/ok1-1",
                                "icon": "el-icon-ks",
                                "sort": 3,
                                "permission": "all",
                                "createAt": "2021-08-08T02:59:13.000Z",
                                "updateAt": "2021-08-08T02:59:13.000Z",
                            }]
                        },
                    ]
                },
            ],
            "totalCount": 1
        }
    }
    return result

@api.delete("/user/{user_id}")
def delete_user(request, user_id: int):
    print(user_id)
    result = {
        "code": 0,
        "data": {
            "msg": f"删除成功{user_id}"
        }
    }
    return result
