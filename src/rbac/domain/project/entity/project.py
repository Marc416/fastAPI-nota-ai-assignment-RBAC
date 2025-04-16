from datetime import datetime

from sqlalchemy import Integer, Column, String, DateTime, Enum as SAEnum

from rbac.application.config.db.base import Base
from rbac.domain.project.entity.project_status import ProjectStatus


class Project(Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True, autoincrement=True)
    owner_id = Column(Integer, nullable=False)
    title = Column(String(255), nullable=False)
    status = Column(SAEnum(ProjectStatus), default=ProjectStatus.ACTIVE, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)

    @classmethod
    def create_active_project(cls, title: str, owner_id: int):
        project = cls(
            title=title,
            owner_id=owner_id,
            status=ProjectStatus.ACTIVE,
        )

        return project

    def update_title(self, new_title: str):
        self.title = new_title
        self.updated_at = datetime.now()

    def delete(self):
        self.status = ProjectStatus.DELETED
        self.deleted_at = datetime.now()
