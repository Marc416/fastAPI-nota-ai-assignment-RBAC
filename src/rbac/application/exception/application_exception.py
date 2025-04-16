from rbac.application.common.http_response.code_enum import CodeEnum


class ApplicationException(Exception):
    def __init__(
            self,
            code: CodeEnum,
            message: str,
            data: dict = None,
    ):
        self.code = code
        self.message = message
        self.data = data
        super().__init__(message)