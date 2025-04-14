from dependency_injector import containers, providers
from sqlalchemy.orm import Session

from rbac.application.account.repository.account_repository_impl import AccountRepositoryImpl
from rbac.application.common.jwt_token_provider_impl import JwtTokenProviderImpl
from rbac.config.db.database import get_db
from rbac.config.settings import Settings
from rbac.domain.account.repository.account_repository import AccountRepository
from rbac.domain.account.service.account_command_service import AccountCommandService
from rbac.domain.account.service.account_command_usercase import AccountCommandUseCase
from rbac.domain.common.jwt_token_provider import JwtTokenProvider


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=["rbac"]
    )

    settings: Settings = providers.Factory(Settings)

    db: providers.Resource[Session] = providers.Resource(get_db)

    jwt_token_provider: JwtTokenProvider = providers.Factory(
        JwtTokenProviderImpl,
        settings=settings
    )

    account_repository: AccountRepository = providers.Factory(AccountRepositoryImpl, db=db)

    account_command_service: AccountCommandUseCase = providers.Factory(
        AccountCommandService,
        account_repository=account_repository,
        jwt_token_provider=jwt_token_provider
    )

