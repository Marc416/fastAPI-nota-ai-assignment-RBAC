from __future__ import annotations
from enum import Enum
from typing import Set


class AccountRole(Enum):
    USER = ("일반 사용자", set())
    ADMIN = ("관리자", "일반 사용자")  # 초기엔 문자열로만 참조

    def __init__(self, description: str, inherited_role_names: Set[str]):
        self.description = description
        self._inherited_role_names = inherited_role_names

    @property
    def inherited_roles(self) -> Set[AccountRole]:
        # 초기 문자열을 enum 인스턴스로 변환
        return {AccountRole[name] for name in self._inherited_role_names}

    def get_all_roles(self) -> Set[AccountRole]:
        roles = {self}
        for role in self.inherited_roles:
            roles.update(role.get_all_roles())
        return roles