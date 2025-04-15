from typing import Optional, List

from dependency_injector.wiring import inject, Provide
from sqlalchemy import and_
from sqlalchemy.orm import Session

from rbac.domain.project.entity.project_member import ProjectMember
from rbac.domain.project.repository.project_member_repository import ProjectMemberRepository


class ProjectMemberRepositoryImpl(ProjectMemberRepository):
    @inject
    def __init__(self, db: Session = Provide["db"]):
        self.db = db

    def save_all(self, members: List[ProjectMember]) -> List[ProjectMember]:
        saved_members = []
        for member in members:
            existing = self.db.query(ProjectMember).filter(
                and_(
                    ProjectMember.account_id == member.account_id,
                    ProjectMember.project_id == member.project_id
                )
            ).first()

            if existing:
                existing.role = member.role
                existing.deleted_at = None
            else:
                self.db.add(member)

            saved_members.append(member)

        self.db.commit()
        return saved_members

    def update_all(self, members: List[ProjectMember]) -> List[ProjectMember]:
        for member in members:
            existing = self.db.query(ProjectMember).filter(
                and_(
                    ProjectMember.account_id == member.account_id,
                    ProjectMember.project_id == member.project_id
                )
            ).first()
            if existing:
                existing.role = member.role
                existing.deleted_at = member.deleted_at

        self.db.commit()
        return members

    def find_by_account_id_and_project_id(
        self, account_id: int, project_id: int
    ) -> Optional[ProjectMember]:
        return self.db.query(ProjectMember).filter(
            and_(
                ProjectMember.account_id == account_id,
                ProjectMember.project_id == project_id,
                ProjectMember.deleted_at.is_(None)
            )
        ).first()

    def find_by_project_id(self, project_id: int) -> List[ProjectMember]:
        return  self.db.query(ProjectMember).filter(
            and_(
                ProjectMember.project_id == project_id,
                ProjectMember.deleted_at.is_(None)
            )
        ).all()
