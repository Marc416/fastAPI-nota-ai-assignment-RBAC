from pydantic import BaseModel


class AccountSigInRequest(BaseModel):
    email: str
    tenant_key: str
    password: str
