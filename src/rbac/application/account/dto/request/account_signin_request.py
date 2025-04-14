from pydantic import BaseModel, EmailStr


class AccountSigInRequest(BaseModel):
    email: EmailStr
    tenant_key: str
    password: str
