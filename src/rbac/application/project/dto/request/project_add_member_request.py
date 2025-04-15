from pydantic import BaseModel

from rbac.domain.project.entity.project_role import ProjectRole


class MemberRequest(BaseModel):
    """
    프로젝트에 추가할 멤버를 나타내는 모델입니다.
    """
    account_id: int
    role: ProjectRole

class ProjectAddMemberRequest(BaseModel):
    """
    프로젝트에 멤버를 추가하는 요청을 나타내는 모델입니다.
    """
    member_requests: list[MemberRequest] = []
