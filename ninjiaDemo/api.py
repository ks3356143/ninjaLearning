from ninja import NinjaAPI, Field, Query, Schema
import orjson
from ninja.parser import Parser
from typing import List

class OrjsonParser(Parser):
    def parse_body(self, request):
        return orjson.loads(request.body)

api = NinjaAPI(parser=OrjsonParser())

class Filters(Schema):
    limit: int = 100
    offset: int = None
    query: str = None
    category__in: List[str] = Field(None, alias="categories")

@api.get("/filter")
def events(request, filters: Filters = Query(...)):
    return {"filters": filters.dict()}
