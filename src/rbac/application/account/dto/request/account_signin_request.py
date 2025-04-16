from pydantic import BaseModel, EmailStr, Field

from rbac.application.account.validator.password_str import PasswordStr


class AccountSigInRequest(BaseModel):
    email: EmailStr
    tenant_key: str
    password: PasswordStr
