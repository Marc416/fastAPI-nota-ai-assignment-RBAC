from abc import ABC, abstractmethod
from typing import List, Optional

from rbac.domain.project.entity.project_member import ProjectMember


class ProjectMemberRepository(ABC):
    @abstractmethod
    def save_all(self, members: List[ProjectMember]) -> List[ProjectMember]:
        raise NotImplementedError()

    @abstractmethod
    def update_all(self, members: List[ProjectMember]) -> List[ProjectMember]:
        raise NotImplementedError()

    @abstractmethod
    def find_by_account_id_and_project_id(self, account_id: int, project_id: int) -> Optional[ProjectMember]:
        raise NotImplementedError()

    @abstractmethod
    def find_by_project_id(self, project_id: int) -> List[ProjectMember]:
        raise NotImplementedError()