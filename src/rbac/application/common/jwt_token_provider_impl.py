from typing import Dict, Any, Container

import jwt
from dependency_injector.wiring import Provide, inject
from fastapi import Depends
from jwt import PyJWTError

from rbac.config.settings import Settings
from rbac.domain.account.dto.account_jwt_payload import AccountJwtPayload
from rbac.domain.common.jwt_token_provider import JwtTokenProvider


class JwtTokenProviderImpl(JwtTokenProvider):

    @inject
    def __init__(self, settings: Settings):
        self.secret_key = settings.jwt_secret_key
        self.algorithm = "HS256"

    def parse_authorization_token(self, token: str) -> AccountJwtPayload:
        decoded = self.__verify_token(token)
        return AccountJwtPayload(**decoded)

    def validate_token(self, token: str) -> bool:
        try:
            self.__verify_token(token)
            return True
        except (PyJWTError, ValueError):
            return False

    def generate_token(self, payload: Dict[str, Any], ttl: int) -> str:
        return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)

    def __verify_token(self, token: str) -> Dict[str, Any]:
        try:
            decoded = jwt.decode(
                token,
                self.secret_key,
                algorithms=[self.algorithm]
            )
            return decoded  # dict 형태로 반환됨
        except PyJWTError as e:
            raise ValueError(f"Invalid JWT token: {e}")
