from pydantic import BaseModel

from rbac.domain.project.entity.project_role import ProjectRole


class MemberRequest(BaseModel):
    account_id: int
    role: ProjectRole