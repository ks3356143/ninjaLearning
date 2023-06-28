from ninja import Router, Schema, Field, ModelSchema
from typing import List
from utils.chen_response import ChenResponse
from ninjaapp.models import Round
from django.shortcuts import get_object_or_404

router = Router()

class SchemaOut(ModelSchema):
    class Config:
        model = Round
        model_exclude = ['remark']

class SchemaIn(ModelSchema):
    class Config:
        model = Round
        model_fields = ['beginTime', 'best_condition_tem', 'best_condition_voltage', 'endTime', 'grade', 'ident',
                        'low_condition_tem', 'low_condition_voltage', 'name', 'package', 'speedGrade',
                        'typical_condition_tem', 'typical_condition_voltage','key']

class EditSchemaIn(Schema):
    beginTime: str
    best_condition_tem: str
    best_condition_voltage: str
    create_datetime: str
    endTime: str
    grade: str
    id: int
    ident: str
    key: str
    level: str
    low_condition_tem: str
    low_condition_voltage: str
    name: str
    package: str
    project: int
    speedGrade: str
    title: str
    update_datetime: str
    typical_condition_tem: str
    typical_condition_voltage: str

class DeleteSchema(Schema):
    title:str
    key:str
    level:str

# 输出树状信息的schema
class treeReturnRound(Schema):
    title: str = Field(..., alias='title')
    key: str = Field(..., alias='key')
    level: str = Field(..., alias='level')

@router.get("/getRoundInfo/{project_id}", response=List[treeReturnRound])
def get_round_tree(request, project_id):
    qs = Round.objects.filter(project__id=project_id).order_by('key')
    return qs

@router.get("/getOneRoundInfo", response=SchemaOut)
def get_round_info(request, projectId: str, round: str):
    qs = Round.objects.filter(project__id=projectId).order_by('id')
    # 将轮次从str -> int类型
    qs = qs[int(round)]
    return qs

@router.put("/round/update/{id}", response=SchemaOut)
def update_user(request, id, payload: EditSchemaIn):
    round = get_object_or_404(Round, project__id=payload.project, id=id)
    # 去重功能
    exist_round = Round.objects.filter(project__id=payload.project)
    for exist_r in exist_round:
        if exist_r.id != int(id):
            if exist_r.ident == payload.ident:
                return ChenResponse(code=400, status=400, message='标识和其他重复')
    for attr, value in payload.dict().items():
        # 不知道为什么多个project
        if attr != "project":
            setattr(round, attr, value)
    round.save()
    return round

@router.post("/round/save", response=SchemaOut)
def create_user(request, project_id: str, data: SchemaIn):
    asert_dict = data.dict()
    asert_dict['project_id'] = int(project_id)
    asert_dict['title'] = asert_dict['name']
    # 标识去重
    exist_round = Round.objects.filter(project__id=project_id)
    for exist_r in exist_round:
        if exist_r.id != int(project_id):
            if exist_r.ident == asert_dict['ident']:
                return ChenResponse(code=400, status=400, message='标识和其他重复')
    qs = Round.objects.create(**asert_dict)
    return qs

@router.delete("/round/delete")
def delete_user(request, project_id:str ,data: DeleteSchema):
    # 先查询该project下面的值
    instance = get_object_or_404(Round,project__id=project_id,key=data.key)
    instance.delete()
    return ChenResponse(message="删除成功")




