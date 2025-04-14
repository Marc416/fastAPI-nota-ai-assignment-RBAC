from abc import ABC, abstractmethod


class EmailVerifyUseCase(ABC):
    @abstractmethod
    def send_verify_email(self, email: str) -> str:
        raise NotImplementedError()

    @abstractmethod
    def verify_email_code(self, email: str, code: int) -> bool:
        raise NotImplementedError()
