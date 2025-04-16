import logging
from typing import List

from dependency_injector.wiring import inject

from rbac.domain.project.dto.request.member_request import MemberRequest
from rbac.domain.project.dto.response.project_response import ProjectResponse
from rbac.domain.project.entity.project import Project
from rbac.domain.project.entity.project_member import ProjectMember
from rbac.domain.project.repository.project_member_repository import ProjectMemberRepository
from rbac.domain.project.repository.project_repository import ProjectRepository
from rbac.domain.project.service.project_command_usecase import ProjectCommandUseCase

logger = logging.getLogger(__name__)

class ProjectCommandService(ProjectCommandUseCase):
    @inject
    def __init__(
            self,
            project_repository: ProjectRepository,
            project_member_repository: ProjectMemberRepository,
    ):
        self.project_repository = project_repository
        self.project_member_repository = project_member_repository

    def add_member(self, project_id: int, member_requests: List[MemberRequest]) -> ProjectResponse:
        project: Project = self.project_repository.get_by_id(project_id)
        project_members = []
        for member_request in member_requests:
            project_member: ProjectMember = ProjectMember.create(
                project_id=project.id,
                account_id=member_request.account_id,
                role=member_request.role,
            )
            project_members.append(project_member)

        self.project_member_repository.save_all(project_members)
        return ProjectResponse(project_id=project.id)


    def remove_member(self, project_id: int, member_ids: List[int]) -> ProjectResponse:
        project: Project = self.project_repository.get_by_id(project_id)
        project_members:List[ProjectMember]= self.project_member_repository.find_by_project_id(project.id)
        # TODO : 이하 리팩터링 필요(기존 jpa에서 사용하던 애그리게이트 개념을 사용할 수 없음-아직 몰라서 못하는듯 )
        member_map = {member.account_id: member for member in project_members}
        members = []
        for member_id in member_ids:
            if member_id not in member_map:
                # 예외처리로 하지 않음.
                logger.warning("Member ID %s not found in project members", member_id)
                continue
            member_map[member_id].remove_from_project()
            members.append(member_map[member_id])
        self.project_member_repository.update_all(members)
        return ProjectResponse(project_id=project.id)

    def update_project(self, project_id: int, new_title: str) -> ProjectResponse:
        project :Project = self.project_repository.get_by_id(project_id)
        project.update_title(new_title)
        self.project_repository.save(project)
        return ProjectResponse(project_id=project.id)

    def delete_project(self, project_id: int) -> ProjectResponse:
        project: Project = self.project_repository.get_by_id(project_id)
        project.delete()
        self.project_repository.save(project)
        return ProjectResponse(project_id=project.id)

    def create_project(self, title: str, owner_id: int, member_requests: List[MemberRequest]) -> ProjectResponse:
        project: Project = Project.create_active_project(
            title=title,
            owner_id=owner_id,
        )
        created_project: Project = self.project_repository.save(project)

        project_members = []
        for member_request in member_requests:
            project_members.append(ProjectMember.create(
                project_id=created_project.id,
                account_id=member_request.account_id,
                role=member_request.role,
            ))
        self.project_member_repository.save_all(project_members)
        return ProjectResponse(project_id=created_project.id)
