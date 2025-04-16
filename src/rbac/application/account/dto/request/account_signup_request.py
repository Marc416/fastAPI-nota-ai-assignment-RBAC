from pydantic import BaseModel, EmailStr, Field

from rbac.application.account.validator.password_str import PasswordStr
from rbac.domain.account.entity.account_role import AccountRole


class AccountSignupRequest(BaseModel):
    email: EmailStr
    password: PasswordStr
    tenant_key: str
    role: AccountRole
