from pydantic import BaseModel


class ProjectResponse(BaseModel):
    project_id: int