from abc import ABC, abstractmethod


class AccountRepository(ABC):
    @abstractmethod
    def save(self):
        raise NotImplementedError

    @abstractmethod
    def find_by_account_id(self):
        raise NotImplementedError()

    @abstractmethod
    def find_by_email_and_tenant_key(self):
        raise NotImplementedError()
