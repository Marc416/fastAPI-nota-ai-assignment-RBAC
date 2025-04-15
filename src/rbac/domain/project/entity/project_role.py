from enum import Enum, auto
from typing import Set
from __future__ import annotations

from fastapi import HTTPException


class ProjectRole(str, Enum):
    # 변수명 을 그대로 value로 사용하기 위해 auto() 메서드를 오버라이드
    # 주의 : 변수명보다 앞서 오버라이드 되어야 함
    def _generate_next_value_(name, start, count, last_values):
        return name  # 변수명을 문자열 그대로 value로 사용

    VIEWER = auto()
    EDITOR = auto()
    PROJECT_OWNER = auto()

    @classmethod
    def from_str(cls, value: str) -> ProjectRole:
        try:
            return cls(value)
        except ValueError:
            raise HTTPException(status_code=400, detail=f"Invalid role: {value}")

ROLE_DESCRIPTIONS = {
    ProjectRole.VIEWER: "뷰어",
    ProjectRole.EDITOR: "편집자",
    ProjectRole.PROJECT_OWNER: "프로젝트 소유자",
}

ROLE_INHERITANCE = {
    ProjectRole.VIEWER: set(),
    ProjectRole.EDITOR: {ProjectRole.VIEWER},
    ProjectRole.PROJECT_OWNER: {ProjectRole.EDITOR},
}

def get_all_roles(role: ProjectRole) -> Set[ProjectRole]:
    roles = {role}
    for inherited in ROLE_INHERITANCE.get(role, set()):
        roles.update(get_all_roles(inherited))
    return roles