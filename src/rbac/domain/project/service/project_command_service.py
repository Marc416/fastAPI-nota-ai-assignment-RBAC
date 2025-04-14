from typing import List

from dependency_injector.wiring import inject

from rbac.domain.project.dto.request.member_request import MemberRequest
from rbac.domain.project.dto.response.project_response import ProjectResponse
from rbac.domain.project.entity.project import Project
from rbac.domain.project.entity.project_member import ProjectMember
from rbac.domain.project.repository.project_member_repository import ProjectMemberRepository
from rbac.domain.project.repository.project_repository import ProjectRepository
from rbac.domain.project.service.project_command_usecase import ProjectCommandUseCase


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
        pass

    def remove_member(self, project_id: int, member_ids: List[int]) -> ProjectResponse:
        pass

    def update_project(self, project_id: int, new_title: str) -> ProjectResponse:
        pass

    def delete_project(self, project_id: int) -> ProjectResponse:
        pass

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
