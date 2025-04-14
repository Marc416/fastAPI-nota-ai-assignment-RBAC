from pydantic import BaseModel


class AccountJwtPayload(BaseModel):
    account_id: int
    tenant_key: str
    role: str
