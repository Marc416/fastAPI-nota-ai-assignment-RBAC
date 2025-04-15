from typing import List

from pydantic import BaseModel


class ProjectRemoveMemberRequest(BaseModel):
    """
    Request model for removing members from a project
    """
    member_ids: List[int] = []
