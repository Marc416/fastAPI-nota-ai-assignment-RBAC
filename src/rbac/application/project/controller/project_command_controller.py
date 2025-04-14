from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from fastapi_utils.cbv import cbv

from rbac.application.common.http_response.http_api_response import HttpApiResponse
from rbac.application.common.user_detail import UserDetail
from rbac.application.project.dto.request.project_create_request import ProjectCreateRequest
from rbac.config.auth.authentication import get_current_user
from rbac.config.container import Container
from rbac.domain.project.dto.response.project_response import ProjectResponse
# from rbac.domain.project.dto.response.project_response import ProjectResponse
from rbac.domain.project.service.project_command_usecase import ProjectCommandUseCase

router = APIRouter(prefix="/project", tags=["project"])


@cbv(router)
class ProjectCommandController:

    @inject
    def __init__(
            self,
            project_command_usecase: ProjectCommandUseCase = Depends(Provide[Container.project_command_usecase])
    ):
        self.project_command_usecase = project_command_usecase

    @router.post("/")
    async def create_project(
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