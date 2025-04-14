from typing import List

from pydantic import BaseModel

from rbac.domain.project.dto.request.member_request import MemberRequest


class ProjectCreateRequest(BaseModel):
    title: str
    member_requests: List[MemberRequest]