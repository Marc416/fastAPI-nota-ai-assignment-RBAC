from typing import Optional

from dependency_injector.wiring import inject, Provide
from sqlalchemy.orm import Session

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

    def find_by_account_id(self):
        pass

    def find_by_email_and_tenant_key(self, email: str, tenant_key: str) -> Account:
        account: Optional[Account] = self.db.query(Account).filter(
            Account.email == email,
            Account.tenant_key == tenant_key
        ).first()
        if account is None:
            # TODO : 회원 없을 때 예외 처리
            raise ValueError("Account not found")
        return account
