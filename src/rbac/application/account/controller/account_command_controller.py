# class AccountCommandController:
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from fastapi_utils.cbv import cbv

from rbac.application.account.dto.request.account_signup_request import AccountSignupRequest
from rbac.config.container import Container
from rbac.domain.account.service.account_command_usercase import AccountCommandUseCase
from rbac.domain.common.jwt_token_provider import JwtTokenProvider

router = APIRouter(prefix="/account", tags=["account"])


@cbv(router)
class AccountCommandController:

    @inject
    def __init__(
            self,
            account_command_usecase: AccountCommandUseCase = Depends(Provide[Container.account_command_service]),
            jwt_token_provider: JwtTokenProvider = Depends(Provide[Container.jwt_token_provider])
    ):
        self.account_command_usecase = account_command_usecase

    @router.post("/signup")
    def get_test(self, request: AccountSignupRequest):
        self.account_command_usecase.sign_up(
            email=request.email,
            password=request.password,
            tenant_key=request.tenant_key,
            role=request.role
        )
        return {}
