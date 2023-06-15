problemData = [
    {
        'id': 1, #~
        'ident': "PT_R2303_001", ##
        "name": "点击返回无效", ##
        'status': '2', ##
        'grade': '4', ##
        'type': '3', ##
        'closeMethod': ['1', '2'],
        'operation': "导入Coverity的分析结果以及源码",
        'expect': "页面正常显示漏洞列表，且切换页面正常",
        'result': '在结果页面报错“查询漏洞描述、修复、跟踪路径详细异常--任务:8885漏洞42306”',
        'rules': '违反人机交互界面特性',
        'suggest': "修改界面逻辑，修改代码处理",
        'postPerson': '尧颖婷',
        'postDate': "2022-02-22",
        'designerPerson': "张大海",
        'designDate': "2022-02-24",
        'verifyPerson': "陈俊亦",
        'verifyDate': '2022-05-28',
        'revokePerson': '陈俊亦',
        'revokeDate': "2023-01-19"
    },
    {
        'id': 2,
        'ident': "PT_R2303_002",
        "name": "代码显示在页面上链接",
        'status': '1',
        'grade': '3',
        'type': '4',
        'closeMethod': ['1'],
        'operation': "查看需求规格书中首页标明的页数",
        'expect': "理应为35页",
        'result': '需求规格书中首页标明的页数不正确，理应为35页，写的是38页',
        'rules': '违反文档审查原则',
        'suggest': "修改文档",
        'postPerson': '尧颖婷',
        'postDate': "2022-02-22",
        'designerPerson': "张大海",
        'designDate': "2022-02-24",
        'verifyPerson': "李鑫",
        'verifyDate': '2022-05-28',
        'revokePerson': '李鑫',
        'revokeDate': "2023-01-19"
    },
    {
        'id': 3,
        'ident': "PT_R2303_003",
        "name": "新增后页面未刷新",
        'status': '3',
        'grade': '1',
        'type': '2',
        'closeMethod': [],
        'operation': "进入特征提取分系统，点击倒序按钮",
        'expect': "页面倒序显示项目",
        'result': '进入特征提取分系统，点击倒序按钮，界面中信息少了编号、提交用户、开始时间、结束时间信息以及持续时间',
        'rules': '违反功能需求',
        'suggest': "按照界面要求倒序排列",
        'postPerson': '李莉',
        'postDate': "2022-02-22",
        'designerPerson': "张大海",
        'designDate': "2022-02-24",
        'verifyPerson': "陈小球",
        'verifyDate': '2022-05-28',
        'revokePerson': '陈俊亦',
        'revokeDate': "2023-01-19"
    },
]
