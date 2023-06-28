# -*- coding: utf-8 -*-
## 将其他模块导入
from ninjaapp.router import system_router, testmanage_router, project_router
from utils.chen_ninja import ChenNinjaAPI

api = ChenNinjaAPI()

# 统一处理server异常
@api.exception_handler(Exception)
def a(request, exc):
    if hasattr(exc, 'errno'):
        return api.create_response(request, data=[], message=str(exc), code=exc.errno)
    else:
        return api.create_response(request, data=[], message=str(exc), code=500)

api.add_router('/system/', system_router)
api.add_router("/testmanage/", testmanage_router)
api.add_router("/project/", project_router)
