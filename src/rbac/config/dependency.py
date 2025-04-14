from fastapi import Depends

from rbac.application.common.jwt_token_provider_impl import JwtTokenProviderImpl
from rbac.config.settings import Settings


def get_settings():
    return Settings()


def get_jwt_provider(settings=Depends(get_settings)):
    return JwtTokenProviderImpl(settings)
