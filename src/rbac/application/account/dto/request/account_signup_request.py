from pydantic import BaseModel

from rbac.domain.account.entity.account_role import AccountRole


class AccountSignupRequest(BaseModel):
    email: str
    password: str
    tenant_key: str
    role: AccountRole