from __future__ import annotations

from enum import Enum, auto
from typing import Set

from fastapi import HTTPException


class ProjectRole(str, Enum):
    # 변수명 을 그대로 value로 사용하기 위해 auto() 메서드를 오버라이드
    # 주의 : 변수명보다 앞서 오버라이드 되어야 함
    def _generate_next_value_(name, start, count, last_values):
        return name  # 변수명을 문자열 그대로 value로 사용

    VIEWER = auto()
    EDITOR = auto()
    PROJECT_OWNER = auto()

    def description(self) -> str:
        return _PROJECT_ROLE_DESCRIPTIONS[self]

    def get_all_roles(self) -> Set[ProjectRole]:
        roles = {self}
        for inherited in _PROJECT_ROLE_INHERITANCE.get(self, set()):
            roles.update(inherited.get_all_roles())
        return roles

    @classmethod
    def from_str(cls, value: str) -> ProjectRole:
        try:
            return cls(value)
        except ValueError:
            raise HTTPException(status_code=400, detail=f"Invalid role: {value}")


_PROJECT_ROLE_DESCRIPTIONS = {
    ProjectRole.VIEWER: "뷰어",
    ProjectRole.EDITOR: "편집자",
    ProjectRole.PROJECT_OWNER: "프로젝트 소유자",
}

_PROJECT_ROLE_INHERITANCE = {
    ProjectRole.VIEWER: set(),
    ProjectRole.EDITOR: {ProjectRole.VIEWER},
    ProjectRole.PROJECT_OWNER: {ProjectRole.EDITOR},
}