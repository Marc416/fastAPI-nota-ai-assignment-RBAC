import dataclasses
from typing import TypeVar, Generic, List

T = TypeVar("T")

@dataclasses.dataclass
class SliceContent(Generic[T]):
    content: List[T]
    next_cursor: str