from ninja import Router, Schema, ModelSchema
from typing import List
from utils.chen_response import ChenResponse
from ninjaapp.models import Dict, DictItem
from django.forms.models import model_to_dict

router = Router()

class DictOut(ModelSchema):
    class Config:
        model = DictItem
        model_fields = ['id', 'title', 'key', 'sort', 'status']

@router.get("/getNoticeList")
def get_notice(request, pageSize, orderBy, orderType):
    item_list = []
    item1 = {"title": "后台公告1:关于加强后端逻辑能力", "created_at": "2022-09-23", "content": "猫眼可见，undefined 是一个鲁棒只读的属性，表面上相当靠谱"}
    item_list.append(item1)
    item2 = {"title": "后台公告2:关于加强前端样式能力", "created_at": "2023-09-23", "content": "由此可见这个是内容"}
    item_list.append(item2)
    return item_list

@router.get("/dataDict/list", response=List[DictOut])
def get_dict(request, code):
    # 先查询
    dict_qs = Dict.objects.get(code=code)
    items = dict_qs.dictItem.filter(status=True)
    return items
