import logging

from fastapi import FastAPI

from rbac.application.account.controller import account_command_controller
from rbac.application.project.controller import project_command_controller
from rbac.utils.life import lifespan


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

app = FastAPI(lifespan=lifespan)


app.include_router(account_command_controller.router)
app.include_router(project_command_controller.router)

