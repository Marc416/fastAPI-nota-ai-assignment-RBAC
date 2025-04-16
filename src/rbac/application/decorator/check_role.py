from functools import wraps

from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.status import HTTP_403_FORBIDDEN

from rbac.application.common.user_detail import UserDetail
from rbac.application.middleware.context import request_context
from rbac.application.config.auth.authentication import get_current_user_from_request
from rbac.domain.account.entity.account_role import AccountRole


def check_role(required_role: AccountRole):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            request: Request = request_context.get()
            user_detail: UserDetail = get_current_user_from_request(request)

            # 권한 체크
            if not has_authority(
                    user_detail=user_detail,
                    required_role=required_role
            ):
                raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="프로젝트 접근 권한이 없습니다")
            return func(*args, **kwargs)
        return wrapper
    return decorator

def has_authority(
        user_detail: UserDetail,
        required_role: AccountRole,
) -> bool:
    return user_detail.role.get_all_roles().__contains__(required_role)