import hashlib
import os

from django.contrib.auth.models import AbstractUser
from django.db import models
from utils.models import CoreModel

STATUS_CHOICES = (
    (0, '禁用'),
    (1, '启用')
)

class Users(AbstractUser, CoreModel):
    username = models.CharField(max_length=150, unique=True, db_index=True, verbose_name='用户账号', help_text="用户账号")
    name = models.CharField(max_length=40, verbose_name="姓名", help_text="姓名")
    avatar = models.TextField(verbose_name="头像", null=True, blank=True, help_text="头像")
    email = models.EmailField(max_length=255, verbose_name="邮箱", null=True, blank=True, help_text="邮箱")
    status = models.CharField(max_length=15, verbose_name='启用状态', help_text="status")
    job = models.CharField(max_length=255, verbose_name='工作', null=True, blank=True, help_text='工作')
    jobName = models.CharField(max_length=255, verbose_name='工作名称', null=True, blank=True, help_text='工作名称')
    organization = models.CharField(max_length=255, verbose_name='工作组织', null=True, blank=True, help_text='工作组织')
    location = models.CharField(max_length=255, verbose_name='住地', null=True, blank=True, help_text='住地')
    locationName = models.CharField(max_length=255, verbose_name='住地名称', null=True, blank=True, help_text='住地名称')
    introduction = models.CharField(max_length=255, verbose_name='自我介绍', null=True, blank=True, help_text='自我介绍')
    personalWebsite = models.CharField(max_length=255, verbose_name='个人网站', null=True, blank=True, help_text='个人网站')
    phone = models.CharField(max_length=255, verbose_name="电话", null=True, blank=True, help_text="电话")
    # registrationDate 需要再CoreModel的create_datetime修改
    accountId = models.CharField(max_length=255, verbose_name="电话", null=True, blank=True, help_text="电话")
    role = models.CharField(max_length=64, verbose_name="角色", null=True, blank=True, help_text="角色")

## 日志记录
class LoginLog(CoreModel):
    LOGIN_TYPE_CHOICES = (
        (1, '普通登录'),
    )
    username = models.CharField(max_length=32, verbose_name="登录用户名", null=True, blank=True, help_text="登录用户名")
    ip = models.CharField(max_length=32, verbose_name="登录ip", null=True, blank=True, help_text="登录ip")
    agent = models.TextField(verbose_name="agent信息", null=True, blank=True, help_text="agent信息")
    browser = models.CharField(max_length=200, verbose_name="浏览器名", null=True, blank=True, help_text="浏览器名")
    os = models.CharField(max_length=200, verbose_name="操作系统", null=True, blank=True, help_text="操作系统")
    continent = models.CharField(max_length=50, verbose_name="州", null=True, blank=True, help_text="州")
    country = models.CharField(max_length=50, verbose_name="国家", null=True, blank=True, help_text="国家")
    province = models.CharField(max_length=50, verbose_name="省份", null=True, blank=True, help_text="省份")
    city = models.CharField(max_length=50, verbose_name="城市", null=True, blank=True, help_text="城市")
    district = models.CharField(max_length=50, verbose_name="县区", null=True, blank=True, help_text="县区")
    isp = models.CharField(max_length=50, verbose_name="运营商", null=True, blank=True, help_text="运营商")
    area_code = models.CharField(max_length=50, verbose_name="区域代码", null=True, blank=True, help_text="区域代码")
    country_english = models.CharField(max_length=50, verbose_name="英文全称", null=True, blank=True,
                                       help_text="英文全称")
    country_code = models.CharField(max_length=50, verbose_name="简称", null=True, blank=True, help_text="简称")
    longitude = models.CharField(max_length=50, verbose_name="经度", null=True, blank=True, help_text="经度")
    latitude = models.CharField(max_length=50, verbose_name="纬度", null=True, blank=True, help_text="纬度")
    login_type = models.IntegerField(default=1, choices=LOGIN_TYPE_CHOICES, verbose_name="登录类型",
                                     help_text="登录类型")

    class Meta:
        db_table = 'system_login_log'
        verbose_name = '登录日志'
        verbose_name_plural = verbose_name
        ordering = ('-create_datetime',)

## 字典以及字典item
class Dict(CoreModel):
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name="字典名称", help_text="字典名称")
    code = models.CharField(max_length=100, blank=True, null=True, verbose_name="编码", help_text="编码")
    status = models.BooleanField(default=True, blank=True, verbose_name="状态", help_text="状态")
    remark = models.CharField(max_length=2000, blank=True, null=True, verbose_name="备注", help_text="备注")

    class Meta:
        db_table = 'system_dict'
        verbose_name = "字典表"
        verbose_name_plural = verbose_name
        ordering = ('sort',)

class DictItem(CoreModel):
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name="显示名称", help_text="显示名称")
    key = models.CharField(max_length=100, blank=True, null=True, verbose_name="实际值", help_text="实际值")
    status = models.BooleanField(default=True, blank=True, verbose_name="状态", help_text="状态")
    dict = models.ForeignKey(to="Dict", db_constraint=False, related_name="dictItem", on_delete=models.CASCADE,
                             help_text="字典")
    remark = models.CharField(max_length=2000, blank=True, null=True, verbose_name="备注", help_text="备注")

    class Meta:
        db_table = 'system_dict_item'
        verbose_name = "字典表item表"
        verbose_name_plural = verbose_name
        ordering = ('sort',)

class Project(CoreModel):
    ident = models.CharField(max_length=64, blank=True, null=True, verbose_name="项目标识",
                             help_text="项目标识")  # 后面加上unique=True
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name="项目名称", help_text="项目名称")
    engin_model = models.CharField(max_length=64, blank=True, null=True, verbose_name="工程型号", help_text="工程型号")
    section_system = models.CharField(max_length=64, blank=True, null=True, verbose_name="分系统", help_text="分系统")
    sub_system = models.CharField(max_length=64, blank=True, null=True, verbose_name="子系统", help_text="子系统")
    device = models.CharField(max_length=64, blank=True, null=True, verbose_name="设备", help_text="设备")
    beginTime = models.DateField(auto_now_add=True, null=True, blank=True, help_text="开始时间", verbose_name="开始时间")
    endTime = models.DateField(auto_now_add=True, null=True, blank=True, help_text="结束时间", verbose_name="结束时间")
    duty_person = models.CharField(max_length=64, verbose_name="负责人", help_text="负责人")
    member = models.JSONField(null=True, blank=True, help_text="项目成员", verbose_name="项目成员", default=[])
    security_level = models.CharField(max_length=8, blank=True, null=True, verbose_name="安全等级", help_text="安全等级")
    test_level = models.JSONField(null=True, blank=True, help_text="测试级别", verbose_name="测试级别", default=[])
    plant_type = models.CharField(max_length=64, blank=True, null=True, verbose_name="平台类型", help_text="平台类型")
    report_type = models.CharField(max_length=64, blank=True, null=True, verbose_name="报告类型", help_text="报告类型")
    language = models.JSONField(null=True, blank=True, help_text="被测语言", verbose_name="被测语言", default=[])
    standard = models.JSONField(null=True, blank=True, help_text="依据标准", verbose_name="依据标准", default=[])
    entrust_ident = models.CharField(max_length=64, blank=True, null=True, verbose_name="委托方标识", help_text="委托方标识")
    entrust_legal = models.CharField(max_length=64, blank=True, null=True, verbose_name="委托方法人", help_text="委托方法人")
    entrust_contact = models.CharField(max_length=64, blank=True, null=True, verbose_name="委托方联系人", help_text="委托方联系人")
    entrust_contact_phone = models.CharField(max_length=64, blank=True, null=True, verbose_name="委托方电话",
                                             help_text="委托方电话")
    entrust_email = models.CharField(max_length=64, blank=True, null=True, verbose_name="委托方邮箱", help_text="委托方邮箱")
    dev_ident = models.CharField(max_length=64, blank=True, null=True, verbose_name="研制方标识", help_text="研制方标识")
    dev_legal = models.CharField(max_length=64, blank=True, null=True, verbose_name="研制方法人", help_text="研制方法人")
    dev_contact = models.CharField(max_length=64, blank=True, null=True, verbose_name="研制方联系人", help_text="研制方联系人")
    dev_contact_phone = models.CharField(max_length=64, blank=True, null=True, verbose_name="研制方电话", help_text="研制方电话")
    dev_email = models.CharField(max_length=64, blank=True, null=True, verbose_name="研制方邮箱", help_text="研制方邮箱")
    test_ident = models.CharField(max_length=64, blank=True, null=True, verbose_name="测评中心标识", help_text="测评中心标识")
    test_legal = models.CharField(max_length=64, blank=True, null=True, verbose_name="测评中心法人", help_text="测评中心法人")
    test_contact = models.CharField(max_length=64, blank=True, null=True, verbose_name="测评中心联系人", help_text="测评中心联系人")
    test_contact_phone = models.CharField(max_length=64, blank=True, null=True, verbose_name="测评中心电话",
                                          help_text="测评中心电话")
    test_email = models.CharField(max_length=64, blank=True, null=True, verbose_name="测评中心邮箱", help_text="测评中心邮箱")
    step = models.CharField(max_length=8, blank=True, null=True, verbose_name="项目阶段", help_text="项目阶段")

    class Meta:
        verbose_name = "项目信息"
        verbose_name_plural = verbose_name
        ordering = ('-create_datetime',)

class Round(CoreModel):
    ident = models.CharField(max_length=64, blank=True, null=True, verbose_name="轮次标识",
                             help_text="轮次标识")  # 后面加上unique=True
    name = models.CharField(max_length=64, blank=True, null=True, verbose_name="轮次名称",
                            help_text="轮次名称")
    beginTime = models.DateField(auto_now_add=True, null=True, blank=True, help_text="开始时间", verbose_name="开始时间")
    endTime = models.DateField(auto_now_add=True, null=True, blank=True, help_text="结束时间", verbose_name="结束时间")
    speedGrade = models.CharField(max_length=64, blank=True, null=True, verbose_name="速度等级", help_text="速度等级")
    package = models.CharField(max_length=64, blank=True, null=True, verbose_name="封装", help_text="封装")
    grade = models.CharField(max_length=64, blank=True, null=True, verbose_name="等级", help_text="等级")
    best_condition_voltage = models.CharField(max_length=64, blank=True, null=True, verbose_name="最优工况电压",
                                              help_text="最优工况电压")
    best_condition_tem = models.CharField(max_length=64, blank=True, null=True, verbose_name="最优工况温度",
                                          help_text="最优工况温度")
    typical_condition_voltage = models.CharField(max_length=64, blank=True, null=True, verbose_name="典型工况电压",
                                                 help_text="典型工况电压")
    typical_condition_tem = models.CharField(max_length=64, blank=True, null=True, verbose_name="典型工况温度",
                                             help_text="典型工况温度")
    low_condition_voltage = models.CharField(max_length=64, blank=True, null=True, verbose_name="最低工况电压",
                                             help_text="最低工况电压")
    low_condition_tem = models.CharField(max_length=64, blank=True, null=True, verbose_name="最低工况温度",
                                         help_text="最低工况温度")
    project = models.ForeignKey(to="Project", db_constraint=False, related_name="pField", on_delete=models.CASCADE,
                                verbose_name='归属项目', help_text='归属项目',related_query_name='pQuery')
    level = models.CharField(max_length=15, verbose_name='树状级别第一级', help_text="树状级别第一级", default='0')
    key = models.CharField(max_length=15, verbose_name='给前端的树状级别', help_text="给前端的树状级别")
    title = models.CharField(max_length=15, verbose_name='给前端的name', help_text="给前端的name")

    class Meta:
        verbose_name = "轮次信息"
        verbose_name_plural = verbose_name
        ordering = ('-create_datetime',)
