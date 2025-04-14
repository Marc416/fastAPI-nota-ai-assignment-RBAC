from pydantic import BaseModel


class VerifyEmailRequest(BaseModel):
    email: str
    code: int