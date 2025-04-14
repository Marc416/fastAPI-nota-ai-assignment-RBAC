from __future__ import annotations
from enum import Enum, auto
from typing import Set

from fastapi import HTTPException


# class AccountRole(Enum):
#     USER = ("일반 사용자", set())
#     ADMIN = ("관리자", "일반 사용자")  # 초기엔 문자열로만 참조
#
#     def __init__(self, description: str, inherited_role_names: Set[str]):
#         self.description = description
#         self._inherited_role_names = inherited_role_names
#
#     @property
#     def inherited_roles(self) -> Set[AccountRole]:
#         # 초기 문자열을 enum 인스턴스로 변환
#         return {AccountRole[name] for name in self._inherited_role_names}
#
#     def get_all_roles(self) -> Set[AccountRole]:
#         roles = {self}
#         for role in self.inherited_roles:
#             roles.update(role.get_all_roles())
#         return roles

class AccountRole(str, Enum):
    # 변수명 을 그대로 value로 사용하기 위해 auto() 메서드를 오버라이드
    # 주의 : 변수명보다 앞서 오버라이드 되어야 함
    def _generate_next_value_(name, start, count, last_values):
        return name  # 변수명을 문자열 그대로 value로 사용

    USER = auto()
    ADMIN = auto()

    @classmethod
    def from_str(cls, value: str) -> "AccountRole":
        try:
            return cls(value)
        except ValueError:
            raise HTTPException(status_code=400, detail=f"Invalid role: {value}")

ROLE_DESCRIPTIONS = {
    AccountRole.USER: "일반 사용자",
    AccountRole.ADMIN: "관리자",
}

ROLE_INHERITANCE = {
    AccountRole.USER: set(),
    AccountRole.ADMIN: {AccountRole.USER},
}

def get_all_roles(role: AccountRole) -> Set[AccountRole]:
    roles = {role}
    for inherited in ROLE_INHERITANCE.get(role, set()):
        roles.update(get_all_roles(inherited))
    return roles