from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv

from rbac.application.account.dto.request.project_remove_member_request import ProjectRemoveMemberRequest
from rbac.application.account.dto.request.project_update_request import ProjectUpdateRequest
from rbac.application.common.http_response.http_api_response import HttpApiResponse
from rbac.application.common.user_detail import UserDetail
from rbac.application.decorator.check_project_role import check_project_role
from rbac.application.project.dto.request.project_add_member_request import ProjectAddMemberRequest
from rbac.application.project.dto.request.project_create_request import ProjectCreateRequest
from rbac.application.config.auth.authentication import get_current_user
from rbac.application.config.container import Container
from rbac.domain.project.dto.response.project_response import ProjectResponse
from rbac.domain.project.entity.project_role import ProjectRole
from rbac.domain.project.service.project_command_usecase import ProjectCommandUseCase

router = APIRouter(prefix="/project", tags=["project-command"])


@cbv(router)
class ProjectCommandController:

    @inject
    def __init__(
            self,
            project_command_usecase: ProjectCommandUseCase = Depends(Provide[Container.project_command_usecase])
    ):
        self.project_command_usecase = project_command_usecase

    @router.post("/")
    @check_project_role(ProjectRole.PROJECT_OWNER)
    def create_project(
            self,
            request: ProjectCreateRequest,
            user_detail: UserDetail = Depends(get_current_user),
    ):
        """
        Create a new project
        """
        response: ProjectResponse = self.project_command_usecase.create_project(
            title=request.title,
            owner_id=user_detail.account_id,
            member_requests=request.member_requests
        )
        return HttpApiResponse.of(response)

    @router.put("/{project_id}")
    @check_project_role(ProjectRole.EDITOR)
    def update_project(
            self,
            project_id: int,
            request: ProjectUpdateRequest,
    ):
        """
        Update an existing project
        """
        response: ProjectResponse = self.project_command_usecase.update_project(
            project_id=project_id,
            new_title=request.title
        )
        return HttpApiResponse.of(response)

    @router.delete("/{project_id}")
    @check_project_role(ProjectRole.PROJECT_OWNER)
    def delete_project(
            self,
            project_id: int,
    ):
        """
        Delete an existing project
        """
        response: ProjectResponse = self.project_command_usecase.delete_project(
            project_id=project_id
        )
        return HttpApiResponse.of(response)


    @router.post("/{project_id}/members")
    @check_project_role(ProjectRole.PROJECT_OWNER)
    def add_member(
            self,
            project_id: int,
            request: ProjectAddMemberRequest,
            user_detail: UserDetail = Depends(get_current_user),
    ):
        """
        Add members to an existing project
        """
        response: ProjectResponse = self.project_command_usecase.add_member(
            project_id=project_id,
            member_requests=request.member_requests
        )
        return HttpApiResponse.of(response)

    @router.delete("/{project_id}/members")
    @check_project_role(ProjectRole.PROJECT_OWNER)
    def remove_member(
            self,
            project_id: int,
            request: ProjectRemoveMemberRequest,
    ):
        """
        Remove members from an existing project
        """
        response: ProjectResponse = self.project_command_usecase.remove_member(
            project_id=project_id,
            member_ids=request.member_ids
        )
        return HttpApiResponse.of(response)