from ninja import NinjaAPI,Schema

api = NinjaAPI()
class HelloSchema(Schema):
    name: str = 'ok'

@api.post("/hello")
def hello(request, data: HelloSchema):
    return f"你好，{data.name}"

@api.get("/math/")
def math(request, a: int, b: int):
    return {"add": a + b, "multiply": a * b}

@api.get("/math/{a}and{b}")
def math(request, a: int, b: int):
    return {"add": a + b, "multiply": a * b}