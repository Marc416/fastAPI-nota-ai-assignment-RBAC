from enum import Enum, auto


class ProjectStatus(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name

    ACTIVE = auto()
    DELETED = auto()
