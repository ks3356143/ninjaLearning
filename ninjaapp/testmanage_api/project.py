from ninja import Router, pagination, Field, Schema, ModelSchema, Query
from utils.chen_ninja import MyPagination
from typing import List
from ninjaapp.models import Project
from utils.chen_response import ChenResponse
from utils.chen_crud import create,multi_delete
from django.shortcuts import get_object_or_404
import json

router = Router()

class SchemaIn(ModelSchema):
    class Config:
        model = Project
        model_exclude = ['remark', 'update_datetime', 'create_datetime', 'sort', 'id']

class ProjectFilterSchema(Schema):
    ident: str = Field(None, alias='ident')
    name: str = Field(None, alias='name')
    duty_person: str = Field(None, alias='duty_person')
    security_level: str = Field(None, alias='security_level')
    report_type: str = Field(None, alias="report_type")
    step: str = Field(None, alias="step")

class SchemaOut(ModelSchema):
    class Config:
        model = Project
        model_exclude = ['update_datetime', 'create_datetime', 'remark']

@router.get("/project/index", response=List[SchemaOut])
@pagination.paginate(MyPagination)
def list_project(request, filters: ProjectFilterSchema = Query(...)):
    for attr, value in filters.__dict__.items():
        if getattr(filters, attr) is None:
            setattr(filters, attr, '')
    # 处理时间范围
    start_time = request.GET.get('searchOnlyTimeRange[0]')
    if start_time is None:
        start_time = "2000-01-01"
    end_time = request.GET.get('searchOnlyTimeRange[1]')
    if end_time is None:
        end_time = '5000-01-01'
    date_list = [start_time, end_time]
    # 前端返回的member
    member_list = []
    for key, value in request.GET.items():
        if key.find('member') != -1:
            member_list.append(request.GET[key])
    qs = Project.objects.filter(ident__icontains=filters.ident, name__icontains=filters.name,
                                beginTime__range=date_list, duty_person__icontains=filters.duty_person,
                                security_level__icontains=filters.security_level,
                                report_type__icontains=filters.report_type, step__icontains=filters.step,
                                member__contains=member_list)
    return qs

@router.post("/project/save", response=SchemaOut)
def create_user(request, data: SchemaIn):
    data_dict = data.dict()
    # 判重-> 也可以在数据库 unique=True
    ident_qucover = Project.objects.filter(ident=data.dict()['ident'])
    if ident_qucover:
        return ChenResponse(code=400, status=400, message="项目标识重复，请重新设置")
    qs = create(request, data_dict, Project)
    return qs

@router.put("/project/update/{project_id}", response=SchemaOut)
def update_user(request, project_id: int, payload: SchemaIn):
    project = get_object_or_404(Project, id=project_id)
    # 更新操作
    for attr, value in payload.dict().items():
        # setattr针对的是class
        setattr(project, attr, value)
    project.save()
    return project

class DeleteSchema(Schema):
    ids: List[int]

@router.delete("/project/delete")
def delete_user(request, data: DeleteSchema):
    multi_delete(data.ids,Project)
    return ChenResponse(message="删除成功！")
