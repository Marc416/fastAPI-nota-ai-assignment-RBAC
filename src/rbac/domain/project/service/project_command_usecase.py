from abc import ABC, abstractmethod
from typing import List

from rbac.domain.project.dto.request.member_request import MemberRequest
from rbac.domain.project.dto.response.project_response import ProjectResponse


class ProjectCommandUseCase(ABC):
    @abstractmethod
    def add_member(self, project_id: int, member_requests: List[MemberRequest]) -> ProjectResponse:
        raise NotImplementedError()

    @abstractmethod
    def remove_member(self, project_id: int, member_ids: List[int]) -> ProjectResponse:
        raise NotImplementedError()

    @abstractmethod
    def update_project(self, project_id: int, new_title: str) -> ProjectResponse:
        raise NotImplementedError()

    @abstractmethod
    def delete_project(self, project_id: int) -> ProjectResponse:
        raise NotImplementedError()

    @abstractmethod
    def create_project(self, title: str, owner_id: int, member_requests: List[MemberRequest]) -> ProjectResponse:
        raise NotImplementedError()
