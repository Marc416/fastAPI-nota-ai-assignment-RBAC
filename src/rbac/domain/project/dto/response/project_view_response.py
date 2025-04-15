from pydantic import BaseModel


class ProjectViewResponse(BaseModel):
    project_id: int
    title: str
    project_owner: int