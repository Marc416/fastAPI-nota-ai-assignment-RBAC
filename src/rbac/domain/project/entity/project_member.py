from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, Enum as SAEnum
from sqlalchemy.orm import declarative_base, relationship

from rbac.config.db.base import Base
from rbac.domain.project.entity.project_role import ProjectRole


class ProjectMember(Base):
    __tablename__ = "project_member"

    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, nullable=False)
    account_id = Column(Integer, nullable=False)
    role :ProjectRole = Column(SAEnum(ProjectRole), nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    deleted_at = Column(DateTime, nullable=True)

    @classmethod
    def create(cls, project_id: int, account_id: int, role: ProjectRole):
        return cls(
            project_id=project_id,
            account_id=account_id,
            role=role,
            created_at=datetime.now(),
        )

    def remove_from_project(self):
        self.deleted_at = datetime.now()
