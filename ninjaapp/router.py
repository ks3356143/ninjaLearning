from ninja import Router
from ninjaapp.apis.login import router as login_router
from ninjaapp.apis.common import router as common_router
from ninjaapp.apis.user import router as user_router
from ninjaapp.apis.round import router as round_router
from ninjaapp.testmanage_api.project import router as project_info_router

system_router = Router()
testmanage_router = Router()
project_router =Router()

# system的ninja路由
system_router.add_router('/', login_router, tags=["Login"])
system_router.add_router('/', common_router, tags=["Common"])
system_router.add_router('/', user_router, tags=["User"])

# testmanage的ninja路由
testmanage_router.add_router("/",project_info_router,tags=["Project"])

# project的ninja路由
project_router.add_router("/",round_router,tags=['Round'])
