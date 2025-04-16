from functools import wraps

from dependency_injector.wiring import Provide
from fastapi import Request, Depends

from rbac.application.common.http_response.code_enum import CodeEnum
from rbac.application.common.user_detail import UserDetail
from rbac.application.config.auth.authentication import get_current_user_from_request
from rbac.application.config.container import Container
from rbac.application.exception.application_exception import ApplicationException
from rbac.application.middleware.context import request_context
from rbac.domain.account.entity.account_role import AccountRole
from rbac.domain.project.entity.project_role import ProjectRole
from rbac.domain.project.repository.project_member_repository import ProjectMemberRepository
from rbac.domain.project.repository.project_repository import ProjectRepository


def check_project_role(required_role: ProjectRole):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            request: Request = request_context.get()
            project_id: int = request.path_params.get("project_id")
            user_detail: UserDetail = get_current_user_from_request(request)
            if not project_id:
                raise ApplicationException(
                    code=CodeEnum.FRS_003,
                    message="프로젝트 ID가 필요합니다"
                )

            if required_role == ProjectRole.VIEWER:
                return func(*args, **kwargs)

            # 권한 체크
            if not has_authority(
                    user_detail=user_detail,
                    project_id=project_id,
                    required_role=required_role
            ):
                raise ApplicationException(
                    code=CodeEnum.FRS_002,
                    message="프로젝트 접근 권한이 없습니다"
                )
            return func(*args, **kwargs)
        return wrapper
    return decorator


def has_authority(
        user_detail: UserDetail,
        project_id: int,
        required_role: ProjectRole,
        project_repository: ProjectRepository = Depends(Provide[Container.project_repository]),
        project_member_repository: ProjectMemberRepository = Depends(Provide[Container.project_member_repository])
) -> bool:
    # 관리자 권한 체크
    if AccountRole.ADMIN in user_detail.role.get_all_roles():
        return True

    # 프로젝트 Owner 권한 체크
    project = project_repository.get_by_id(project_id)
    if required_role == ProjectRole.PROJECT_OWNER and project.owner_id == user_detail.account_id:
        return True

    # 사용자가 project_member 테이블에서 권한을 가지고 있는지 확인
    project_member = project_member_repository.find_by_account_id_and_project_id(
        account_id=user_detail.account_id,
        project_id=project_id
    )
    if project_member is None:
        return False

    return project_member.role.get_all_roles().__contains__(required_role)