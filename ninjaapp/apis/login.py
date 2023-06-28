# from django.core.cache import cache
from django.forms.models import model_to_dict
from ninja import Router, ModelSchema, Query, Schema, Field
from ninjaapp.models import Users
from utils.chen_response import ChenResponse
import jwt

router = Router()

class SchemaOut(ModelSchema):
    class Config:
        model = Users
        model_exclude = ['password']

class LoginSchema(Schema):
    username: str = Field(None, alias="username")
    password: str = Field(None, alias="password")
    code: str


@router.post("/login")
def login(request, data: LoginSchema):
    if data.username == "superAdmin":
        if data.password == 'admin123':
            b = {'username': data.username, 'password': data.password}
            token = jwt.encode(b, 'secret', algorithm='HS256')
            return ChenResponse(code=200, data={'token': token})
        else:
            return ChenResponse(status=500, code=500, message="账号或密码错误")

@router.get("/getInfo")
def get_userinfo(request):
    user = Users.objects.get(id=1)
    user_obj_dic = model_to_dict(user)
    user_obj_dic.pop("password")
    response_data = user_obj_dic
    return response_data

@router.post("/logout")
def logout(request):
    return ChenResponse(code=200,message='退出登录成功')