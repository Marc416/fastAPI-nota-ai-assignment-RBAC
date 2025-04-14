from pydantic import BaseModel


class AccountJwtPayload(BaseModel):
    account_id: int
    tenant_key: str
    role: str

    def to_map(self) -> dict:
        return {
            "account_id": self.account_id,
            "tenant_key": self.tenant_key,
            "role": self.role
        }