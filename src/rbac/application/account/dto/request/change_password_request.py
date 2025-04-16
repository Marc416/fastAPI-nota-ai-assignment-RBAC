from pydantic import BaseModel, Field

from rbac.application.account.validator.password_str import PasswordStr


class ChangePasswordRequest(BaseModel):
    new_password: PasswordStr
