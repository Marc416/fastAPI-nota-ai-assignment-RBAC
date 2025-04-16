from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from fastapi_utils.cbv import cbv

from rbac.application.common.http_response.http_api_response import HttpApiResponse
from rbac.application.config.container import Container
from rbac.domain.project.dto.response.project_view_response import ProjectViewResponse
from rbac.domain.project.service.project_query_usecase import ProjectQueryUseCase
from rbac.utils.slice_content import SliceContent

router = APIRouter(prefix="/project", tags=["project-query"])


@cbv(router)
class ProjectQueryController:
    @inject
    def __init__(
            self,
            projectQueryUseCase: ProjectQueryUseCase = Depends(Provide[Container.project_query_usecase])
    ):
        self.project_query_usecase = projectQueryUseCase

    @router.get("/")
    def get_projects(self, size: int = 10, next_cursor: str = None):
        response: SliceContent[ProjectViewResponse] = self.project_query_usecase.get_projects(
            size=size, next_cursor=next_cursor
        )
        return HttpApiResponse.of(data=response)
