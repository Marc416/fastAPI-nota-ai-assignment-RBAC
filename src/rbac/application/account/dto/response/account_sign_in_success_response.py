from pydantic import BaseModel


class AccountSignInSuccessResponse(BaseModel):
    token: str
