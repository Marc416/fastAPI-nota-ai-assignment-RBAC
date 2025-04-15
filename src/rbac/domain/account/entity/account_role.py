from __future__ import annotations
from enum import Enum, auto
from typing import Set

from fastapi import HTTPException

class AccountRole(str, Enum):
    # 변수명 을 그대로 value로 사용하기 위해 auto() 메서드를 오버라이드
    # 주의 : 변수명보다 앞서 오버라이드 되어야 함
    def _generate_next_value_(name, start, count, last_values):
        return name  # 변수명을 문자열 그대로 value로 사용


    USER = auto()
    ADMIN = auto()

    def description(self) -> str:
        return _ACCOUNT_ROLE_DESCRIPTIONS[self]

    def get_all_roles(self) -> Set[AccountRole]:
        roles = {self}
        for inherited in _ACCOUNT_ROLE_INHERITANCE.get(self, set()):
            roles.update(inherited.get_all_roles())
        return roles

    @classmethod
    def from_str(cls, value: str) -> AccountRole:
        try:
            return cls(value)
        except ValueError:
            raise HTTPException(status_code=400, detail=f"Invalid role: {value}")


_ACCOUNT_ROLE_DESCRIPTIONS = {
    AccountRole.USER: "일반 사용자",
    AccountRole.ADMIN: "관리자",
}

_ACCOUNT_ROLE_INHERITANCE = {
    AccountRole.USER: set(),
    AccountRole.ADMIN: {AccountRole.USER},
}