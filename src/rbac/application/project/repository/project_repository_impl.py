from typing import Optional

from dependency_injector.wiring import inject, Provide
from sqlalchemy import and_
from sqlalchemy.orm import Session

from rbac.application.common.http_response.code_enum import CodeEnum
from rbac.application.exception.application_exception import ApplicationException
from rbac.domain.project.entity.project import Project
from rbac.domain.project.entity.project_status import ProjectStatus
from rbac.domain.project.repository.project_repository import ProjectRepository
from rbac.utils.slice_content import SliceContent


class ProjectRepositoryImpl(ProjectRepository):
    @inject
    def __init__(self, db: Session = Provide["db"]):
        self.db = db

    def save(self, project: Project) -> Project:
        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)
        return project

    def get_by_id(self, id: int) -> Project:
        project: Optional[Project] = self.db.query(Project).filter(
            and_(
                Project.id == id,
                Project.status == ProjectStatus.ACTIVE
            )
        ).first()
        if project is None:
            raise ApplicationException(
                code=CodeEnum.FRS_001,
                message="Project not found",
            )
        return project

    def find_by_id(self, id: int) -> Optional[Project]:
        project: Optional[Project] = self.db.query(Project).filter(
            and_(
                Project.id == id,
                Project.status == ProjectStatus.ACTIVE
            )
        ).first()
        return project

    def get_projects(self, size: int, next_cursor: Optional[str]) -> SliceContent[Project]:
        query = self.db.query(Project)

        if next_cursor:
            cursor_val = int(next_cursor)
            # 커서 이후의 ID만 조회
            query = query.filter(
                and_(
                    Project.id <= cursor_val,
                    Project.status == ProjectStatus.ACTIVE
                )
            )

        query = query.order_by(Project.id.desc()).limit(size + 1)  # +1로 다음 커서가 있는지 확인

        projects = query.all()

        has_next = len(projects) > size
        if has_next:
            next_cursor_value = projects[-1].id
            projects = projects[:-1]  # 마지막은 다음 커서니까 제외
        else:
            next_cursor_value = None

        return SliceContent[Project](
            content=projects,
            next_cursor=str(next_cursor_value) if next_cursor_value else None
        )
