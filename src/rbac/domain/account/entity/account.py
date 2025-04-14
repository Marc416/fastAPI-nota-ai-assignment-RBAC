from datetime import datetime

from passlib.context import CryptContext
from sqlalchemy import Column, String, Integer, Enum as SAEnum, DateTime
from sqlalchemy.orm import declarative_base

from rbac.domain.account.entity.account_role import AccountRole
from rbac.domain.account.entity.account_status import AccountStatus

Base = declarative_base()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Account(Base):
    __tablename__ = "account"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    tenant_key = Column(String(255), nullable=False)
    role = Column(SAEnum(AccountRole), nullable=False)
    status = Column(SAEnum(AccountStatus), default=AccountStatus.ACTIVE, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    deleted_at = Column(DateTime, nullable=True)

    # Factory method (companion object)
    @classmethod
    def create_active_account(cls, email: str, raw_password: str, tenant_key: str, role: AccountRole):
        return cls(
            email=email,
            password=pwd_context.hash(raw_password),
            tenant_key=tenant_key,
            role=role,
            status=AccountStatus.ACTIVE,
        )

    # Password change method
    def change_password(self, new_password: str):
        self.password = pwd_context.hash(new_password)

    # Password check
    def is_password_valid(self, input_password: str) -> bool:
        return pwd_context.verify(input_password, self.password)

    # Soft delete
    def delete(self):
        self.status = AccountStatus.INACTIVE
        self.deleted_at = datetime.now()