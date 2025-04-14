from enum import Enum, auto


class CodeEnum(str, Enum):
    # 변수명 을 그대로 value로 사용하기 위해 auto() 메서드를 오버라이드
    # 주의 : 변수명보다 앞서 오버라이드 되어야 함
    def _generate_next_value_(name, start, count, last_values):
        return name  # 변수명을 문자열 그대로 value로 사용

    RS_000 = auto()
    RS_001 = auto()
    RS_002 = auto()
    RS_003 = auto()
    RS_004 = auto()


    @property
    def description(self):
        return {
            CodeEnum.RS_000: "성공",
            CodeEnum.RS_001: "데이터 없음",
            CodeEnum.RS_002: "권한 없음",
            CodeEnum.RS_003: "Invalid Request",
            CodeEnum.RS_004: "Unknown Error",
        }[self]
