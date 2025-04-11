from src.rbac.application.common.jwt_token_provider_impl import JwtTokenProviderImpl
from src.rbac.config.settings import Settings


class TestJwtTokenProvider:
    def test_토큰생성검사(self):
        # Arrange
        settings = Settings()
        jwt_token_provider = JwtTokenProviderImpl(settings=settings)
        payload = {
            "user": "hello"
        }
        # Act
        token: str = jwt_token_provider.generate_token(payload=payload, ttl=60)
        # Assert
        result: bool = jwt_token_provider.validate_token(token=token)
        assert result == True
