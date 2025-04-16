from pydantic import BaseModel

from rbac.application.project.validator.project_title_str import ProjectTitleStr


class ProjectUpdateRequest(BaseModel):
    title: ProjectTitleStr
