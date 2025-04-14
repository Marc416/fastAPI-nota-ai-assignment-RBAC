from datetime import datetime

from pydantic import BaseModel


class AccountSignupSuccessResponse(BaseModel):
    id: int
    created_at: datetime