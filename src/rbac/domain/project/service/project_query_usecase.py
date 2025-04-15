from abc import ABC, abstractmethod

from rbac.domain.project.dto.response.project_view_response import ProjectViewResponse
from rbac.utils.slice_content import SliceContent


class ProjectQueryUseCase(ABC):
    """
    프로젝트 조회를 위한 UseCase 인터페이스입니다.
    """
    @abstractmethod
    def get_projects(self, size: int, next_cursor: str) -> SliceContent[ProjectViewResponse]:
        raise NotImplementedError