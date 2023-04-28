from django.db.models import Q
from ninja import NinjaAPI, FilterSchema, Schema, Field, Query
from typing import Optional,List
import orjson
from ninja.parser import Parser
from datetime import date

class OrjsonParser(Parser):
    def parse_body(self, request):
        return orjson.loads(request.body)

api = NinjaAPI(parser=OrjsonParser())

# 使用filter函数
class EmployeeFilterSchema(FilterSchema):
    def custom_expression(self) -> Q:
        q = Q()

    first_name: Optional[str] = Field(q='first_name__icontains')
    age: Optional[str]

class EmployeeOut(Schema):
    id:int
    first_name:str
    last_name:str
    department_id: int = None
    birthdate:date

from ninjaapp.models import Employee

@api.get("/employee",response=List[EmployeeOut])
def list_employee(request, filters: EmployeeFilterSchema = Query(...)):
    employees = Employee.objects.filter(filters.first_name)
    return employees
