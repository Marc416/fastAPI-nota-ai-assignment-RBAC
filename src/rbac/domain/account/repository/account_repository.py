from abc import ABC, abstractmethod

from rbac.domain.account.entity.account import Account


class AccountRepository(ABC):
    @abstractmethod
    def save(self):
        raise NotImplementedError

    @abstractmethod
    def find_by_account_id(self):
        raise NotImplementedError()

    @abstractmethod
    def find_by_email_and_tenant_key(self, email: str, tenant_key: str) -> Account:
        raise NotImplementedError()
