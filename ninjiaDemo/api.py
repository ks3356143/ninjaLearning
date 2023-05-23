from ninja.parser import Parser
from ninja.renderers import BaseRenderer
from ninja import NinjaAPI, Query, FilterSchema, Field, Schema, ModelSchema
from typing import Optional, List, Any
from datetime import date
import orjson
from ninjaapp.models import Employee
from django.db.models import Q

class OrjsonParser(Parser):
    def parse_body(self, request):
        return orjson.loads(request.body)

class OrjsonRenderer(BaseRenderer):
    media_type = "application/json"
    def render(self, request, data, *, response_status: int) -> Any:
        return orjson.dumps(data)

api = NinjaAPI(parser=OrjsonParser(),renderer=OrjsonRenderer())

class EmployeeFilterSchema(FilterSchema):
    id: Optional[int] = Field(q="id__contains")
    age: Optional[int]
    birthdate: Optional[date]

class EmployeeOut(ModelSchema):
    class Config:
        model = Employee
        model_fields = ['id']

@api.get("/books", response=List[EmployeeOut])
def list_books(request, filters: EmployeeFilterSchema = Query(...)):
    q = filters.get_filter_expression()
    employee = Employee.objects.filter(q)
    print(employee)
    return employee
