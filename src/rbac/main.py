import logging

from fastapi import FastAPI

from rbac.application.account.controller import account_command_controller
from rbac.application.exception.controller_exception_handler import register_exception_handlers
from rbac.application.middleware.request_context_middleware import RequestContextMiddleware
from rbac.application.project.controller import project_command_controller, project_query_controller
from rbac.application.experiment.controller import experiment_query_controller
from rbac.utils.life import lifespan

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

app = FastAPI(lifespan=lifespan)
app.add_middleware(RequestContextMiddleware)
register_exception_handlers(app)

app.include_router(account_command_controller.router)
app.include_router(project_command_controller.router)

app.include_router(project_query_controller.router)
app.include_router(experiment_query_controller.router)
