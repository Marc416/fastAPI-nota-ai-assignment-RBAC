from rbac.domain.account.port.out.email_service_port import EmailServicePort


class EmailServicePortStubImpl(EmailServicePort):
    def send(self, email: str, code: str) -> bool:
        # 이메일 전송 로직
        return True
