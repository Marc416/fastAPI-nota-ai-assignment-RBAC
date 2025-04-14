from pydantic import BaseModel

from rbac.domain.account.entity.account_role import AccountRole


class UserDetail(BaseModel):
    account_id: int
    tenant_key: str
    role: AccountRole