from abc import ABC, abstractmethod

from rbac.application.account.dto.response.account_sign_in_success_response import AccountSignInSuccessResponse
from rbac.application.account.dto.response.account_signup_success_response import AccountSignupSuccessResponse
from rbac.domain.account.entity.account_role import AccountRole


class AccountCommandUseCase(ABC):
    @abstractmethod
    def sign_up(
            self,
            email: str,
            password: str,
            tenant_key: str,
            role: AccountRole,
    ) -> AccountSignupSuccessResponse:
        raise NotImplementedError()

    @abstractmethod
    def sign_in(self, email: str, tenantKey: str, password: str) -> AccountSignInSuccessResponse:
        raise NotImplementedError()

    @abstractmethod
    def chang_password(self, user_id: int, newPassword: str):
        raise NotImplementedError()

    @abstractmethod
    def delete_account(self, accountId: int):
        raise NotImplementedError()

    @abstractmethod
    def test(self):
        raise NotImplementedError()