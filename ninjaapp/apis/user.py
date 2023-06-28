from ninja import Router, Schema, Query, Field, ModelSchema
from ninja.pagination import paginate
from typing import List
from utils.chen_response import ChenResponse
from utils.chen_crud import create, multi_delete
from utils.chen_ninja import MyPagination
from ninjaapp.models import Users,Project
from django.shortcuts import get_object_or_404

router = Router()

class UserFilterSchema(Schema):
    username: str = Field(None, alias='username')
    name: str = Field(None, alias='name')
    phone: str = Field(None, alias='phone')
    status: str = Field(None, alias='status')

class SchemaOut(ModelSchema):
    class Config:
        model = Users
        model_exclude = ['password']

class SchemaIn(ModelSchema):
    class Config:
        model = Users
        model_fields = ['email', 'name', 'password', 'phone', 'status', 'username']

@router.get("/user/index", response=List[SchemaOut])
@paginate(MyPagination)
def list_user(request, filters: UserFilterSchema = Query(...)):
    for attr, value in filters.__dict__.items():
        if getattr(filters, attr) is None:
            setattr(filters, attr, '')
    start_time = request.GET.get('create_datetime[0]')
    if start_time is None:
        start_time = "2000-01-01"
    end_time = request.GET.get('create_datetime[1]')
    if end_time is None:
        end_time = '5000-01-01'
    date_list = [start_time, end_time]
    qs = Users.objects.filter(name__icontains=filters.name, username__icontains=filters.username,
                              phone__icontains=filters.phone, status__contains=filters.status,
                              create_datetime__range=date_list)
    return qs

@router.post("/user/save", response=SchemaOut)
def create_user(request, data: SchemaIn):
    data_dict = data.dict()
    # 判重
    inuser = Users.objects.filter(username=data.dict()['username'])
    if inuser:
        return ChenResponse(code=400, status=400, message="账号重复，请重新设置")
    user = create(request, data_dict, Users)
    return user

@router.put("/user/update/{user_id}", response=SchemaOut)
def update_user(request, user_id: int, payload: SchemaIn):
    # get_object_or_404默认调用get方法，如果查询对象不存在返回前端404
    user = get_object_or_404(Users, id=user_id)
    if user_id == 1:
        return ChenResponse(code=400, status=400, message="无法编辑，唯一账号")
    # 更新操作
    for attr, value in payload.dict().items():
        # setattr针对的是class
        setattr(user, attr, value)
    user.save()
    return user

class DeleteSchema(Schema):
    ids: List[int]

@router.delete("/user/delete")
def delete_user(request, data: DeleteSchema):
    multi_delete(data.ids,Users)
    return ChenResponse(message="删除成功！")

# 单独给前端要下拉框看用户信息设置
@router.get("/user/list",response=List[SchemaOut])
def all_list_user(request):
    qs = Users.objects.all()
    return qs
