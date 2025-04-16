from dependency_injector.wiring import inject

from rbac.application.account.dto.response.account_sign_in_success_response import AccountSignInSuccessResponse
from rbac.application.account.dto.response.account_signup_success_response import AccountSignupSuccessResponse
from rbac.application.common.http_response.code_enum import CodeEnum
from rbac.application.exception.application_exception import ApplicationException
from rbac.domain.account.dto.account_jwt_payload import AccountJwtPayload
from rbac.domain.account.entity.account import Account
from rbac.domain.account.entity.account_role import AccountRole
from rbac.domain.account.repository.account_repository import AccountRepository
from rbac.domain.account.service.account_command_usercase import AccountCommandUseCase
from rbac.domain.common.jwt_token_provider import JwtTokenProvider


class AccountCommandService(AccountCommandUseCase):

    @inject
    def __init__(
            self,
            account_repository: AccountRepository,
            jwt_token_provider: JwtTokenProvider
    ):
        self.account_repository = account_repository
        self.jwt_token_provider = jwt_token_provider

    def sign_up(self, email: str, password: str, tenant_key: str,
                role: AccountRole) -> AccountSignupSuccessResponse:
        account: Account = Account.create_active_account(email, password, tenant_key, role)
        self.account_repository.save(account)
        return AccountSignupSuccessResponse(
            id=account.id,
            created_at=account.created_at
        )

    def sign_in(self, email: str, tenant_key: str, password: str) -> AccountSignInSuccessResponse:
        account: Account = self.account_repository.find_by_email_and_tenant_key(
            email=email,
            tenant_key=tenant_key
        )

        if (not account.is_password_valid(password)):
            raise ApplicationException(code= CodeEnum.FRS_003, message="Invalid password")

        account_payload_map = AccountJwtPayload(
            account_id=account.id,
            tenant_key=account.tenant_key,
            role=account.role
        ).to_map()
        token = self.jwt_token_provider.generate_token(payload=account_payload_map, ttl=60 * 60 * 24 * 7)  # 7일
        return AccountSignInSuccessResponse(token=token)

    def change_password(self, account_id: int, new_password: str):
        account: Account = self.account_repository.get_by_account_id(id=account_id)
        account.change_password(new_password=new_password)
        self.account_repository.save(account)
        pass

    def delete_account(self, account_id: int):
        account: Account = self.account_repository.get_by_account_id(id=account_id)
        account.delete()
        self.account_repository.save(account)
        pass
