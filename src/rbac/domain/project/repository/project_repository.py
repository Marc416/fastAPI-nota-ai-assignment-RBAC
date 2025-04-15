from abc import abstractmethod, ABC
from typing import Optional

from rbac.domain.project.entity.project import Project
from rbac.utils.slice_content import SliceContent


class ProjectRepository(ABC):
    @abstractmethod
    def save(self, project: Project) -> Project:
        raise NotImplementedError()

    @abstractmethod
    def get_by_id(self, id: int) -> Project:
        raise NotImplementedError()

    @abstractmethod
    def find_by_id(self, id: int) -> Optional[Project]:
        raise NotImplementedError()

    @abstractmethod
    def get_projects(self, size: int, next_cursor: Optional[str]) -> SliceContent[Project]:
        raise NotImplementedError()
