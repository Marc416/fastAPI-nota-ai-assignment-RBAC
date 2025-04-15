from typing import Optional, List

from dependency_injector.wiring import inject

from rbac.domain.project.dto.response.project_view_response import ProjectViewResponse
from rbac.domain.project.entity.project import Project
from rbac.domain.project.repository.project_repository import ProjectRepository
from rbac.domain.project.service.project_query_usecase import ProjectQueryUseCase
from rbac.utils.slice_content import SliceContent


class ProjectQueryService(ProjectQueryUseCase):
    @inject
    def __init__(
            self,
            project_repository: ProjectRepository,
    ):
        self.project_repository = project_repository

    def get_projects(self, size: int, next_cursor: Optional[str]) -> SliceContent[ProjectViewResponse]:
        result: SliceContent[Project] = self.project_repository.get_projects(size=size, next_cursor=next_cursor)
        content: List[ProjectViewResponse] = [
            ProjectViewResponse(project_id=project.id, title=project.title, project_owner=project.owner_id) for project
            in result.content]
        return SliceContent(
            content=content,
            next_cursor=result.next_cursor,
        )
