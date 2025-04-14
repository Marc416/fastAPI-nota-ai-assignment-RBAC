from pydantic import BaseModel


class EmailVerifyRequest(BaseModel):
    email: str