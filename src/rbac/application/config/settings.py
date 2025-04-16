from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    대문자환경변수를 사용하는 설정 클래스
    ex) JWT_SECRET_KEY(OS) -> jwt_secret_key(Python)
    """
    jwt_secret_key: str = "mysecretkey"
    database_conn: str = "mysql+mysqlconnector://root:root1234@localhost:13306/account"

    class Config:
        env_file = None
        extra = "ignore"
