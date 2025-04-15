from pydantic import BaseModel


class ProjectUpdateRequest(BaseModel):
    title: str
