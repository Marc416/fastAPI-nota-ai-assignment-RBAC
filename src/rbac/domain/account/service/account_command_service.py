from ast import Index

from dependency_injector.wiring import inject

from rbac.application.account.dto.response.account_sign_in_success_response import AccountSignInSuccessResponse
from rbac.application.account.dto.response.account_signup_success_response import AccountSignupSuccessResponse
from rbac.domain.account.entity.account_role import AccountRole
from rbac.domain.account.repository.account_repository import AccountRepository
from rbac.domain.account.service.account_command_usercase import AccountCommandUseCase


class AccountCommandService(AccountCommandUseCase):
    def test(self):
        print("test")

    @inject
    def __init__(
            self,
            account_repository: AccountRepository
    ):
        self.account_repository = account_repository


    def sign_up(self, email: str, password: str, tenant_key: str,
                role: AccountRole) -> AccountSignupSuccessResponse:
        pass

    def sign_in(self, email: str, tenant_key: str, password: str) -> AccountSignInSuccessResponse:
        pass

    def chang_password(self, user_id: int, new_password: str):
        pass

    def delete_account(self, account_id: int):
        pass
