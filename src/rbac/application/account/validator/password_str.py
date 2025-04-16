from typing import Annotated

from pydantic import StringConstraints

PasswordStr = Annotated[str, StringConstraints(min_length=6, max_length=255)]
