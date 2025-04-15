from dependency_injector.wiring import Provide, inject
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError
from starlette.requests import Request

from rbac.application.common.user_detail import UserDetail
from rbac.config.container import Container
from rbac.domain.account.entity.account_role import AccountRole
from rbac.domain.common.jwt_token_provider import JwtTokenProvider

bearer_scheme = HTTPBearer()


@inject
def get_current_user(
        credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
        jwt_token_provider: JwtTokenProvider = Depends(Provide[Container.jwt_token_provider]),
) -> dict:
    token = credentials.credentials
    try:
        payload = jwt_token_provider.parse_authorization_token(token)

        return UserDetail(account_id=payload.account_id, tenant_key=payload.tenant_key,
                          role=AccountRole.from_str(payload.role))
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")


def get_current_user_from_request(request: Request, jwt_token_provider: JwtTokenProvider = Depends(Provide[Container.jwt_token_provider])) -> UserDetail:
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid Authorization header")

    token = auth_header.removeprefix("Bearer ").strip()
    try:
        payload = jwt_token_provider.parse_authorization_token(token)
        return UserDetail(
            account_id=payload.account_id,
            tenant_key=payload.tenant_key,
            role=AccountRole.from_str(payload.role)
        )
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")