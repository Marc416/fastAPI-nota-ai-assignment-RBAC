from fastapi import FastAPI

from rbac.application.account.controller import account_command_controller
from rbac.config.container import Container
from rbac.utils.life import lifespan

# from utils.life import lifespan

app = FastAPI(lifespan=lifespan)


app.include_router(account_command_controller.router)

