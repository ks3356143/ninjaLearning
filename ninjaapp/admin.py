from django.contrib import admin
from django.contrib.admin import ModelAdmin

#自定义类展示
class ShowDepartment(ModelAdmin):
    list_display = ['id','title']
    list_display_links = ['title']
class ShowEmployee(ModelAdmin):
    list_display = ['id','last_name','age','birthdate','department_id']
    list_display_links = ['last_name']
# Register your models here.
from .models import Department,Employee
admin.site.register(Department,ShowDepartment)
admin.site.register(Employee,ShowEmployee)
