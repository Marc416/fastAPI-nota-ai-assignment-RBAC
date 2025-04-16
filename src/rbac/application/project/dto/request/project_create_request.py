from typing import List

from pydantic import BaseModel

from rbac.application.project.validator.project_title_str import ProjectTitleStr
from rbac.domain.project.dto.request.member_request import MemberRequest


class ProjectCreateRequest(BaseModel):
    title: ProjectTitleStr
    member_requests: List[MemberRequest]