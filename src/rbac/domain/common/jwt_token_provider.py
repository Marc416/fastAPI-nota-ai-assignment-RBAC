from abc import ABC, abstractmethod
from typing import Dict, Any

from rbac.domain.account.dto.account_jwt_payload import AccountJwtPayload


class JwtTokenProvider(ABC):
    @abstractmethod
    def parse_authorization_token(self, token: str) -> AccountJwtPayload:
        raise NotImplementedError()

    @abstractmethod
    def validate_token(self, token: str) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def generate_token(self, payload: Dict[str, Any], ttl: int) -> str:
        raise NotImplementedError()
