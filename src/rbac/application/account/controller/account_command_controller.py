# class AccountCommandController:
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, FastAPI, Depends
from fastapi_utils.cbv import cbv

from rbac.application.account.repository.account_repository_impl import AccountRepositoryImpl
from rbac.config.container import Container
from rbac.domain.account.repository.account_repository import AccountRepository
from rbac.domain.account.service.account_command_service import AccountCommandService
from rbac.domain.account.service.account_command_usercase import AccountCommandUseCase
from rbac.domain.common.jwt_token_provider import JwtTokenProvider

router = APIRouter(prefix="/help", tags=["blogs"])


@cbv(router)
class AccountCommandController:
    # account_command_usecase: AccountCommandUseCase = Depends(Provide[Container.account_command_service])
    @inject
    def __init__(
            self,
            account_command_usecase: AccountCommandUseCase = Depends(Provide[Container.account_command_service]),
            jwt_token_provider :JwtTokenProvider = Depends(Provide[Container.jwt_token_provider] )
    ):
        self.account_command_usecase = account_command_usecase

    @router.get("/")
    def get_test(self):
        AccountCommandService(
            account_repository=AccountRepositoryImpl()
        )
        self.account_command_usecase.test()
        return {}
