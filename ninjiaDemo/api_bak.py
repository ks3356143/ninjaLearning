from ninja import NinjaAPI, Schema, Form
from typing import List
from datetime import date
import jwt

api = NinjaAPI()

class LoginSchema(Schema):
    username: str
    password: str
    code: str

result = {"success": True, "message": "请求成功", "code": 200, "data": {
    "token": ""
}}

@api.post("/system/login")
def login(request, data: LoginSchema):
    name = data.username
    password = data.password
    b = {'name': name, 'password': password}
    token = jwt.encode(b, 'secret', algorithm='HS256')
    result["data"]["token"] = token
    return result

@api.post("/system/logout")
def logout(request):
    return result

@api.get("/system/getInfo")
def info(request):
    role = 'admin'
    result["data"] = {
        "username": "superAdmin",
        "name": '陈小球',
        "avatar": '//lf1-xgcdn-tos.pstatp.com/obj/vcloud/vadmin/start.8e0e4855ee346a46ccff8ff3e24db27b.png',
        "email": 'wangliqun@email.com',
        "job": 'frontend',
        "jobName": '前端艺术家',
        "organization": 'Frontend',
        "organizationName": '前端',
        "location": 'chengdu',
        "locationName": '成都',
        "introduction": '这是我的自我介绍',
        "personalWebsite": 'https://www.arco.design',
        "phone": '18782947123',
        "registrationDate": '2013-05-10 12:10:00',
        "accountId": '15012312300',
        "certification": 1,
        "role": role
    }
    return result

# 获取公共信息接口
class itemSchema(Schema):
    title: str
    created_at: date

@api.get("/common/getNoticeList")
def get_notice(request, pageSize, orderBy, orderType):
    item_list = []
    item1 = {"title": "后台公告1:关于加强后端逻辑能力", "created_at": "2022-09-23", "content": "猫眼可见，undefined 是一个鲁棒只读的属性，表面上相当靠谱"}
    item_list.append(item1)
    item2 = {"title": "后台公告2:关于加强前端样式能力", "created_at": "2023-09-23", "content": "由此可见这个是内容"}
    item_list.append(item2)
    result['data'] = item_list
    print(result)
    return result

# ~~~~~~~~~~~用户页面接口~~~~~~~~~~~~
## 用户根据page和pageSize查询接口
@api.get("/system/user/index")
def get_user_list(request, page=1, pageSize=10):
    print(page, pageSize)
    result['data'] = [
        {
            "id": 1,
            "name": "尧颖婷",
            "username": "admin",
            "data_scope": 1,
            "status": 1,
            "sort": 1,
            "created_by": 1,
            "updated_by": 1,
            "email": "314298729@qq.com",
            "created_at": "2022-11-07 13:59:52",
            "updated_at": "2023-03-30 16:42:26",
            "phone": '18782947123',
            "introduce": "ok,我是自我介绍"
        },
        {
            "id": 2,
            "name": "陈小球",
            "username": "superadmin",
            "data_scope": 1,
            "status": 1,
            "sort": 1,
            "created_by": 1,
            "updated_by": 1,
            "email": "314298729@qq.com",
            "created_at": "2022-11-07 13:59:52",
            "updated_at": "2023-03-30 16:42:26",
            "phone": '18782947123',
            "introduce": "ok,我是自我介绍"
        },
        {
            "id": 3,
            "name": "陈大球",
            "username": "admin",
            "data_scope": 2,
            "status": 1,
            "sort": 1,
            "created_by": 1,
            "updated_by": 1,
            "email": "314298729@qq.com",
            "created_at": "2022-11-07 14:18:09",
            "updated_at": "2023-03-30 16:42:36",
            "phone": '13782947123',
            "introduce": "ok,我是自我介绍"
        },
        {
            "id": 4,
            "name": "卢俊义",
            "username": "admin",
            "data_scope": 3,
            "status": 1,
            "sort": 1,
            "created_by": 1,
            "updated_by": 1,
            "email": "314298729@qq.com",
            "created_at": "2022-11-07 14:23:30",
            "updated_at": "2023-03-30 16:41:59",
            "phone": '18882947123',
            "introduce": "ok,我是自我介绍"
        },
        {
            "id": 5,
            "name": "XXX员工",
            "username": "user",
            "data_scope": 5,
            "status": 1,
            "sort": 1,
            "created_by": 2,
            "updated_by": 2,
            "email": "314298729@qq.com",
            "created_at": "2022-11-17 11:27:20",
            "updated_at": "2023-03-30 16:41:25",
            "phone": '12782947123',
            "introduce": "ok,我是自我介绍"
        },
        {
            "id": 6,
            "name": "cpu测试人员",
            "username": "user",
            "data_scope": 4,
            "status": 1,
            "sort": 1,
            "created_by": 1,
            "updated_by": 1,
            "email": "314298729@qq.com",
            "created_at": "2023-03-30 16:41:11",
            "updated_at": "2023-03-30 16:41:52",
            "phone": '18182947123'
        },
        {
            "id": 7,
            "name": "李鑫",
            "username": "user",
            "data_scope": 4,
            "status": 1,
            "sort": 1,
            "created_by": 1,
            "updated_by": 1,
            "email": "314298729@qq.com",
            "created_at": "2023-03-30 16:41:11",
            "updated_at": "2023-03-30 16:41:52",
            "phone": '18182947123'
        },
        {
            "id": 8,
            "name": "宋敏",
            "username": "user",
            "data_scope": 4,
            "status": 1,
            "sort": 1,
            "created_by": 1,
            "updated_by": 1,
            "email": "314298729@qq.com",
            "created_at": "2023-03-30 16:41:11",
            "updated_at": "2023-03-30 16:41:52",
            "phone": '18182947123'
        },
        {
            "id": 9,
            "name": "李莉",
            "username": "user",
            "data_scope": 4,
            "status": 1,
            "sort": 1,
            "created_by": 1,
            "updated_by": 1,
            "email": "314298729@qq.com",
            "created_at": "2023-03-30 16:41:11",
            "updated_at": "2023-03-30 16:41:52",
            "phone": '18182947123'
        },
        {
            "id": 10,
            "name": "故原",
            "username": "user",
            "data_scope": 4,
            "status": 1,
            "sort": 1,
            "created_by": 1,
            "updated_by": 1,
            "email": "314298729@qq.com",
            "created_at": "2023-03-30 16:41:11",
            "updated_at": "2023-03-30 16:41:52",
            "phone": '18182947123'
        },
        {
            "id": 11,
            "name": "风格",
            "username": "user",
            "data_scope": 4,
            "status": 1,
            "sort": 1,
            "created_by": 1,
            "updated_by": 1,
            "email": "314298729@qq.com",
            "created_at": "2023-03-30 16:41:11",
            "updated_at": "2023-03-30 16:41:52",
            "phone": '18182947123'
        },
        {
            "id": 12,
            "name": "陈鹏",
            "username": "user",
            "data_scope": 4,
            "status": 1,
            "sort": 1,
            "created_by": 1,
            "updated_by": 1,
            "email": "314298729@qq.com",
            "created_at": "2023-03-30 16:41:11",
            "updated_at": "2023-03-30 16:41:52",
            "phone": '18182947123'
        },
        {
            "id": 13,
            "name": "王光宗",
            "username": "user",
            "data_scope": 4,
            "status": 1,
            "sort": 1,
            "created_by": 1,
            "updated_by": 1,
            "email": "314298729@qq.com",
            "created_at": "2023-03-30 16:41:11",
            "updated_at": "2023-03-30 16:41:52",
            "phone": '18182947123'
        },
        {
            "id": 14,
            "name": "翁上力",
            "username": "user",
            "data_scope": 4,
            "status": 1,
            "sort": 1,
            "created_by": 1,
            "updated_by": 1,
            "email": "314298729@qq.com",
            "created_at": "2023-03-30 16:41:11",
            "updated_at": "2023-03-30 16:41:52",
            "phone": '18182947123'
        },
        {
            "id": 15,
            "name": "张敏",
            "username": "user",
            "data_scope": 4,
            "status": 1,
            "sort": 1,
            "created_by": 1,
            "updated_by": 1,
            "email": "314298729@qq.com",
            "created_at": "2023-03-30 16:41:11",
            "updated_at": "2023-03-30 16:41:52",
            "phone": '18182947123'
        },
    ]
    return result

## 用户新增接口
@api.post("/system/user/save")
def add_user(request, data=Form(...)):
    print(data)
    return result

## 用户更新接口
@api.post("/system/user/update/{id}")
def user_update(request):
    return result

## 用户半删除接口
@api.delete("/system/user/delete")
def user_delete(request):
    return result

## 用户真实删除接口
@api.delete("/system/user/realDelete")
def user_realDelete(request):
    return result

## 用户恢复接口
@api.put("/system/user/recovery")
def user_recovery(request):
    return result

# 公共接口：字典查询
@api.get("/system/dataDict/list")
def get_dict(request, code):
    print(code)
    if code == 'data_status':
        result['data'] = [{'id': 7, 'title': '正常', "key": '1'}, {'id': 8, 'title': '停用', "key": '2'}]
    if code == 'report_type':
        result['data'] = [{'id': 1, 'title': '可编程逻辑器件软件仿真验证报告(二方)', "key": '1'},
                          {'id': 2, 'title': '可编程逻辑器件软件配置项三方测评报告', "key": '2'},
                          {'id': 3, 'title': '可编程逻辑器件软件配置项确认测试报告(二方)', "key": '3'},
                          {'id': 4, 'title': '处理器软件单元测试报告(二方)', "key": '4'},
                          {'id': 5, 'title': '处理器软件部件测试报告(二方）', "key": '5'},
                          {'id': 6, 'title': '处理器软件配置项三方测评报告', "key": '6'},
                          {'id': 7, 'title': '处理器软件配置项确认测试报告（二方)', "key": '7'},
                          {'id': 8, 'title': '系统测试报告(二方)', "key": '8'},
                          {'id': 9, 'title': '鉴定测评报告', "key": '9'},
                          ]
    if code == 'step':
        result['data'] = [{'id': 1, 'key': "1", 'title': "刚开始"}, {'id': 2, 'key': "2", 'title': "进行中"},
                          {'id': 3, 'key': "3", 'title': "已完成"},
                          {'id': 4, 'key': "4", 'title': "已废除"}, ]
    if code == 'security_level':
        result['data'] = [{'id': 1, 'key': '1', 'value': "A"}, {'id': 2, 'key': '2', 'value': "B"},
                          {'id': 3, 'key': '3', 'value': "C"},
                          {'id': 4, 'key': '4', 'value': "D"}]
    if code == 'test_level':
        result['data'] = [{'id': 1, 'key': '1', 'title': '分系统测试'}, {'id': 2, 'key': '2', 'title': '单元测试'},
                          {'id': 3, 'key': '3', 'title': '子系统测试'}, {'id': 4, 'key': '4', 'title': '系统测试'},
                          {'id': 5, 'key': '5', 'title': '部件测试'}, {'id': 6, 'key': '6', 'title': '配置项测试'},
                          ]
    if code == 'plant_type':
        result['data'] = [{'id': 1, 'key': '1', 'title': '可编程逻辑器件'}, {'id': 2, 'key': '2', 'title': '嵌入式处理器'},
                          {'id': 3, 'key': '3', 'title': '嵌入式操作系统'}, {'id': 4, 'key': '4', 'title': '桌面操作系统'}]
    if code == 'language':
        result['data'] = [{'id': 1, 'title': 'C', "key": '1'}, {'id': 2, 'title': 'C#', "key": '2'},
                          {'id': 3, 'title': 'C++', "key": '3'}, {'id': 4, 'title': 'Java', "key": '4'},
                          {'id': 5, 'title': 'Python', "key": '5'}, {'id': 6, 'title': 'Verilog', "key": '6'},
                          {'id': 7, 'title': 'VHDL', "key": '7'}, {'id': 8, 'title': 'Rust', "key": '8'},
                          {'id': 9, 'title': 'JavaScript', "key": '9'}, {'id': 10, 'title': 'Golang', "key": '10'},
                          {'id': 11, 'title': '其他请在字典里加', "key": '11'}, ]
    if code == 'standard':
        result['data'] = [{'id': 1, 'title': 'GJB 10157', "key": '1'}, {'id': 2, 'title': 'GJB 438b', "key": '2'},
                          {'id': 3, 'title': 'GJB 9433-2018', "key": '3'}, {'id': 4, 'title': 'GJB/Z 141', "key": '4'},
                          {'id': 5, 'title': 'BTCG-001', "key": '5'}, {'id': 6, 'title': 'BTCG-002', "key": '6'},
                          {'id': 7, 'title': 'BTCG-003', "key": '7'}, {'id': 8, 'title': 'BTCG-004', "key": '8'},
                          {'id': 9, 'title': 'BTCG-005', "key": '9'}, {'id': 10, 'title': 'BTCG-006', "key": '10'},
                          {'id': 11, 'title': 'BTCG-007', "key": '11'}, ]
    return result

# ~~~~~~~~~~~项目管理页面~~~~~~~~~~~~
from ninjiaDemo.testDir.projectList import projectList

@api.get("/testmanage/project/index")
def project_list(request, page, pageSize):
    result['data'] = projectList
    return result
