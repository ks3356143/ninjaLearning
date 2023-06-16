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
            "name": "陈俊亦",
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
    if code == 'demandType':
        result['data'] = [{"id": 1, 'title': "功能", "key": "1"}, {"id": 2, 'title': "性能", "key": "2"},
                          {"id": 3, 'title': "接口", "key": "3"}, {"id": 4, 'title': "可靠性", "key": "4"},
                          {"id": 5, 'title': "安全性", "key": "5"}, {"id": 6, 'title': "其他", "key": "6"}, ]
    if code == 'priority':
        result['data'] = [{"id": 1, 'title': "高", "key": "1"}, {"id": 2, 'title': "中", "key": "2"},
                          {"id": 3, 'title': "低", "key": "3"}]
    if code == 'testType':
        result['data'] = [{"id": 1, 'title': "代码审查", "key": "1"}, {"id": 2, 'title': "代码走查", "key": "2"},
                          {"id": 3, 'title': "功能测试", "key": "3"}, {"id": 4, 'title': "接口测试", "key": "4"},
                          {"id": 5, 'title': "性能测试", "key": "5"}, {"id": 6, 'title': "安全性测试", "key": "6"},
                          {"id": 7, 'title': "文档审查", "key": "7"}, {"id": 8, 'title': "边界测试", "key": "8"},
                          {"id": 9, 'title': "余量测试", "key": "9"}, {"id": 10, 'title': "强度测试", "key": "10"},
                          {"id": 11, 'title': "人机交互界面测试", "key": "11"}, {"id": 12, 'title': "逻辑测试", "key": "12"},
                          {"id": 13, 'title': "恢复性测试", "key": "13"}, {"id": 14, 'title': "静态分析", "key": "14"},
                          {"id": 15, 'title': "功耗分析", "key": "15"}, {"id": 16, 'title': "时序测试", "key": "16"}, ]
    if code == 'passType':
        result['data'] = [{"id": 1, 'title': "通过", "key": "1"}, {"id": 2, 'title': "未通过", "key": "2"},
                          {"id": 3, 'title': "未执行", "key": "3"}, ]
    if code == 'execType':
        result['data'] = [{"id": 1, 'title': "完整执行", "key": "1"}, {"id": 2, 'title': "部分执行", "key": "2"},
                          {"id": 3, 'title': "未执行", "key": "3"}, ]
    if code == 'problemStatu':
        result['data'] = [{"id": 1, 'title': "关闭", "key": "1"}, {"id": 2, 'title': "开放", "key": "2"},
                          {"id": 3, 'title': "推迟", "key": "3"}, {"id": 4, 'title': "撤销", "key": "4"}, ]
    if code == 'problemType':
        result['data'] = [{"id": 1, 'title': "其他问题", "key": "1"}, {"id": 2, 'title': "文档问题", "key": "2"},
                          {"id": 3, 'title': "程序问题", "key": "3"}, {"id": 4, 'title': "设计问题", "key": "4"}, ]
    if code == 'problemGrade':
        result['data'] = [{"id": 1, 'title': "一般", "key": "1"}, {"id": 2, 'title': "严重", "key": "2"},
                          {"id": 3, 'title': "建议", "key": "3"}, {"id": 4, 'title': "致命", "key": "4"}, ]
    if code == 'closeMethod':
        result['data'] = [{"id": 1, 'title': "修改文档", "key": "1"}, {"id": 2, 'title': "修改程序", "key": "2"}, ]
    return result

# ~~~~~~~~~~~项目管理页面~~~~~~~~~~~~
from ninjiaDemo.testDir.projectList import projectList

@api.get("/testmanage/project/index")
def project_list(request, page, pageSize):
    result['data'] = projectList
    return result

# ~~~~~~~~~~~~树状节点获取~~~~~~~~~~~~
## 树第一层：round
from ninjiaDemo.testDir.treeData import roundData, demandData, testdemandTreeData, caseTreeData, problemTreeData

@api.get("/project/getRoundInfo/{projectId}")
def get_round(request, projectId):
    print(projectId)
    return roundData

## 树第二层：设计需求
@api.get("/project/getDesignDemandInfo")
def get_demand(request, projectId, key, level):
    print('项目id:', projectId)
    print('树key:', key)
    print('树level:', level)
    return demandData

from ninjiaDemo.testDir.designDemand import designDemandData

@api.get("/project/getDesignDemandList")
def getDesignDemandList(request, page, pageSize, projectId, round):
    print('项目id为：', projectId)
    print('轮次为：', round)
    result['data'] = designDemandData
    return result

## 树第三层：测试需求
@api.get("/project/getTestdemandInfo")
def get_demand(request, projectId, key, level):
    print('项目id:', projectId)
    print('树key:', key)
    print('树level:', level)
    return testdemandTreeData

from ninjiaDemo.testDir.testDemand import testDemandData

@api.get("/project/getTestDemandList")
def get_test_demand(request, page, pageSize, projectId, round, designDemand):
    print('项目id为：', projectId)
    print('轮次为：', round)
    print('设计需求为：', designDemand)
    result['data'] = testDemandData
    return result

## 树第四层：测试用例
@api.get("/project/getCaseInfo")
def get_demand(request, projectId, key, level):
    print('项目id:', projectId)
    print('树key:', key)
    print('树level:', level)
    return caseTreeData

from ninjiaDemo.testDir.caseData import caseData

@api.get("/project/getCaseList")
def get_case(request, page, pageSize, projectId, round, designDemand, testDemand):
    print('项目id为：', projectId)
    print('轮次为：', round)
    print('设计需求为：', designDemand)
    print('测试需求为：', testDemand)
    result['data'] = caseData
    return result

## 树第五层：问题单
@api.get("/project/getProblemInfo")
def get_demand(request, projectId, key, level):
    print('项目id:', projectId)
    print('树key:', key)
    print('树level:', level)
    return problemTreeData

from ninjiaDemo.testDir.problemData import problemData

@api.get("/project/getProblemList")
def get_case(request, page, pageSize, projectId, round, designDemand, testDemand, case):
    print('项目id为：', projectId)
    print('轮次为：', round)
    print('设计需求为：', designDemand)
    print('测试需求为：', testDemand)
    print('用例为：', case)
    result['data'] = problemData
    return result

## 树第六层：问题单单个展示样子
@api.get('/project/getSingleProblem')
def get_single_problem(request, projectId, round, designDemand, testDemand, case, problem):
    print('项目id为：', projectId)
    print('轮次为：', round)
    print('设计需求为：', designDemand)
    print('测试需求为：', testDemand)
    print('用例为：', case)
    print('问题单编号为：', problem)
    result['data'] = problemData[2]
    return result
