import logging

from fastapi import FastAPI

from rbac.application.account.controller import account_command_controller
from rbac.application.middleware.request_context_middleware import RequestContextMiddleware
from rbac.application.project.controller import project_command_controller, project_query_controller
from rbac.utils.life import lifespan

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

app = FastAPI(lifespan=lifespan)
app.add_middleware(RequestContextMiddleware)
# TODO app.handler가 등록이 안돼서 임의적으로 실행시키려고 임포트하였는데 다른 방법을 찾아봐야 할거 같음.
import rbac.application.exception.controller_exception_handler as exception_handler
exception_handler
app.include_router(account_command_controller.router)
app.include_router(project_command_controller.router)

app.include_router(project_query_controller.router)
