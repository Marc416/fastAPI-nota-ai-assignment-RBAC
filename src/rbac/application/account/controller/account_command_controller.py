from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from fastapi_utils.cbv import cbv

from rbac.application.account.dto.request.account_signin_request import AccountSigInRequest
from rbac.application.account.dto.request.account_signup_request import AccountSignupRequest
from rbac.application.account.dto.request.change_password_request import ChangePasswordRequest
from rbac.application.account.dto.response.account_signin_success_response import AccountSignInSuccessResponse
from rbac.application.common.http_response.http_api_response import HttpApiResponse
from rbac.application.common.user_detail import UserDetail
from rbac.config.auth.authentication import get_current_user
from rbac.config.container import Container
from rbac.domain.account.service.account_command_usercase import AccountCommandUseCase

router = APIRouter(prefix="/account", tags=["account"])


@cbv(router)
class AccountCommandController:

    @inject
    def __init__(
            self,
            account_command_usecase: AccountCommandUseCase = Depends(Provide[Container.account_command_service]),
    ):
        self.account_command_usecase = account_command_usecase

    @router.post("/signup")
    def sign_up(self, request: AccountSignupRequest):
        self.account_command_usecase.sign_up(
            email=request.email,
            password=request.password,
            tenant_key=request.tenant_key,
            role=request.role
        )
        return {}

    @router.post("/signin")
    def sign_in(self, request: AccountSigInRequest):
        response: AccountSignInSuccessResponse = self.account_command_usecase.sign_in(
            email=request.email,
            tenant_key=request.tenant_key,
            password=request.password
        )
        return HttpApiResponse.of(data=response)

    @router.patch("/password")
    def change_password(
            self,
            change_password_request: ChangePasswordRequest,
            user: UserDetail = Depends(get_current_user),
    ):
        self.account_command_usecase.chang_password(
            account_id=user.account_id, new_password=change_password_request.new_password
        )
        return HttpApiResponse.ok()

    @router.delete("/{account_id}")
    def delete_account(
            self,
            account_id: int,
    ):
        self.account_command_usecase.delete_account(account_id=account_id)
        return HttpApiResponse.ok()
