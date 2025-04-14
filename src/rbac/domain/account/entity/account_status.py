from enum import Enum, auto


class AccountStatus(str, Enum):
    # 변수명 을 그대로 value로 사용하기 위해 auto() 메서드를 오버라이드
    # 주의 : 변수명보다 앞서 오버라이드 되어야 함
    def _generate_next_value_(name, start, count, last_values):
        return name  # 변수명을 문자열 그대로 value로 사용

    ACTIVE = auto()
    INACTIVE = auto()

    @property
    def description(self) -> str:
        return {
            AccountStatus.ACTIVE: "활성",
            AccountStatus.INACTIVE: "비활성"
        }[self]