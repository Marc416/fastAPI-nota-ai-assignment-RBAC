from pydantic import BaseModel, EmailStr


class EmailVerifyRequest(BaseModel):
    email: EmailStr