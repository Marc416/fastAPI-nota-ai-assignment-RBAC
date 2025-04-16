from typing import Optional

from dependency_injector.wiring import inject, Provide
from sqlalchemy.orm import Session

from rbac.application.common.http_response.code_enum import CodeEnum
from rbac.application.exception.application_exception import ApplicationException
from rbac.domain.account.entity.account import Account
from rbac.domain.account.repository.account_repository import AccountRepository


class AccountRepositoryImpl(AccountRepository):
    @inject
    def __init__(self, db: Session = Provide["db"]):
        self.db = db

    def save(self, account: Account) -> Account:
        self.db.add(account)
        self.db.commit()
        self.db.refresh(account)
        return account

    def get_by_account_id(self, id: int) -> Account:
        account: Optional[Account] = self.db.query(Account).filter(
            Account.id == id
        ).first()
        if account is None:
            raise ApplicationException(code= CodeEnum.FRS_001, message="Account not found")
        return account

    def find_by_email_and_tenant_key(self, email: str, tenant_key: str) -> Account:
        account: Optional[Account] = self.db.query(Account).filter(
            Account.email == email,
            Account.tenant_key == tenant_key
        ).first()
        if account is None:
            raise ApplicationException(code= CodeEnum.FRS_001, message="Account not found")
        return account
