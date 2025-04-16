from typing import Annotated

from pydantic import StringConstraints

ProjectTitleStr = Annotated[str, StringConstraints(min_length=1, max_length=255)]
