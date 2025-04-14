import logging
import random
from typing import Dict

from dependency_injector.wiring import inject

from rbac.domain.account.port.out.email_service_port import EmailServicePort
from rbac.domain.account.service.email_verify_usecase import EmailVerifyUseCase

logger = logging.getLogger(__name__)


class EmailVerifyInMemoryService(EmailVerifyUseCase):
    @inject
    def __init__(self, email_service_port):
        self.verification_codes: Dict[str, str] = {}
        self.email_service_port: EmailServicePort = email_service_port

    def send_verify_email(self, email: str) -> str:
        code = self.__generate_verification_code()
        self.verification_codes[email] = code
        self.email_service_port.send(email=email, code=code)
        logger.info(f"Verification code for {email} was sent with code {code}")
        return code

    def verify_email_code(self, email: str, code: int) -> bool:
        return self.verification_codes[email] == (str(code))

    def __generate_verification_code(self) -> str:
        return str(random.randint(100000, 999999))
