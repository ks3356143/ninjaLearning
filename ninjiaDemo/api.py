from ninja import NinjaAPI, Schema, Field
import orjson
from ninja.parser import Parser
from django.contrib.auth.models import User
from ninjaapp.models import Task
from typing import List, Optional

class OrjsonParser(Parser):
    def parse_body(self, request):
        return orjson.loads(request.body)

api = NinjaAPI(parser=OrjsonParser())

class UserSchema(Schema):
    id: int
    first_name: str
    last_name: str

class TaskSchema(Schema):
    id: int
    title: str
    completed: str = Field(..., alias="is_completed")
    owner: Optional[str]
    lower_title: str
    @staticmethod
    def resolve_owner(obj):
        if not obj.owner:
            return
        return f"{obj.owner.first_name} {obj.owner.last_name}"
    def resolve_lower_title(self,obj):
        return self.title.lower()

@api.get("/tasks", response=List[TaskSchema])
def tasks(request):
    queryset = Task.objects.select_related("owner")
    return queryset


