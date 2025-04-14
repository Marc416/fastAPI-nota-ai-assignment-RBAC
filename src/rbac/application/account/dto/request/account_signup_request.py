from pydantic import BaseModel, EmailStr

from rbac.domain.account.entity.account_role import AccountRole


class AccountSignupRequest(BaseModel):
    email: EmailStr
    password: str
    tenant_key: str
    role: AccountRole