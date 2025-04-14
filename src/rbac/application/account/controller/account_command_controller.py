from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from fastapi_utils.cbv import cbv

from rbac.application.account.dto.request.account_signin_request import AccountSigInRequest
from rbac.application.account.dto.request.account_signup_request import AccountSignupRequest
from rbac.application.account.dto.request.change_password_request import ChangePasswordRequest
from rbac.application.account.dto.request.email_verify_request import EmailVerifyRequest
from rbac.application.account.dto.request.verify_email_request import VerifyEmailRequest
from rbac.application.account.dto.response.account_signin_success_response import AccountSignInSuccessResponse
from rbac.application.common.http_response.http_api_response import HttpApiResponse
from rbac.application.common.user_detail import UserDetail
from rbac.config.auth.authentication import get_current_user
from rbac.config.container import Container
from rbac.domain.account.service.account_command_usercase import AccountCommandUseCase
from rbac.domain.account.service.email_verify_usecase import EmailVerifyUseCase

router = APIRouter(prefix="/account", tags=["account"])


@cbv(router)
class AccountCommandController:

    @inject
    def __init__(
            self,
            account_command_usecase: AccountCommandUseCase = Depends(Provide[Container.account_command_usecase]),
            email_verify_usecase: EmailVerifyUseCase = Depends(Provide[Container.email_verify_usecase]),
    ):
        self.account_command_usecase = account_command_usecase
        self.email_verify_usecase = email_verify_usecase

    @router.post("/signup")
    def sign_up(self, request: AccountSignupRequest):
        response: AccountSignInSuccessResponse = self.account_command_usecase.sign_up(
            email=request.email,
            password=request.password,
            tenant_key=request.tenant_key,
            role=request.role
        )
        return HttpApiResponse.of(data= response)

    @router.post("/signin")
    def sign_in(self, request: AccountSigInRequest):
        response: AccountSignInSuccessResponse = self.account_command_usecase.sign_in(
            email=request.email,
            tenant_key=request.tenant_key,
            password=request.password
        )
        return HttpApiResponse.of(data=response)

    @router.post("/verify/email")
    def verify_email(self, request: EmailVerifyRequest):
        self.email_verify_usecase.send_verify_email(email=request.email)
        return HttpApiResponse.ok()

    @router.post("/verify/email/code")
    def verify_email_code(self, request: VerifyEmailRequest):
        self.email_verify_usecase.verify_email_code(email=request.email, code=request.code)
        return HttpApiResponse.ok()

    @router.patch("/password")
    def change_password(
            self,
            change_password_request: ChangePasswordRequest,
            user: UserDetail = Depends(get_current_user),
    ):
        self.account_command_usecase.change_password(
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
