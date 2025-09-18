from dependency_injector import containers, providers
from sqlalchemy.orm import Session

from rbac.application.account.port.out.email_serivce_port_stub_impl import EmailServicePortStubImpl
from rbac.application.account.repository.account_repository_impl import AccountRepositoryImpl
from rbac.application.common.jwt_token_provider_impl import JwtTokenProviderImpl
from rbac.application.config.db.database import get_db
from rbac.application.config.settings import Settings
from rbac.application.experiment.repository.experiment_repository_impl import ExperimentRepositoryImpl
from rbac.application.project.repository.project_member_repository_impl import ProjectMemberRepositoryImpl
from rbac.application.project.repository.project_repository_impl import ProjectRepositoryImpl
from rbac.domain.account.repository.account_repository import AccountRepository
from rbac.domain.account.service.account_command_service import AccountCommandService
from rbac.domain.account.service.account_command_usercase import AccountCommandUseCase
from rbac.domain.account.service.email_verify_service import EmailVerifyInMemoryService
from rbac.domain.account.service.email_verify_usecase import EmailVerifyUseCase
from rbac.domain.common.jwt_token_provider import JwtTokenProvider
from rbac.domain.experiment.repository.experiment_repository import ExperimentRepository
from rbac.domain.experiment.service.experiment_query_service import ExperimentQueryService
from rbac.domain.experiment.usecase.experiment_query_usecase import ExperimentQueryUseCase
from rbac.domain.project.repository.project_member_repository import ProjectMemberRepository
from rbac.domain.project.repository.project_repository import ProjectRepository
from rbac.domain.project.service.project_command_service import ProjectCommandService
from rbac.domain.project.service.project_command_usecase import ProjectCommandUseCase
from rbac.domain.project.service.project_query_service import ProjectQueryService
from rbac.domain.project.service.project_query_usecase import ProjectQueryUseCase


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=["rbac"]
    )

    settings: Settings = providers.Singleton(Settings)

    db: providers.Factory[Session] = providers.Factory(get_db)

    jwt_token_provider: JwtTokenProvider = providers.Singleton(
        JwtTokenProviderImpl,
        settings=settings
    )

    email_verify_usecase: EmailVerifyUseCase = providers.Singleton(
        EmailVerifyInMemoryService,
        email_service_port=EmailServicePortStubImpl()
    )

    account_repository: AccountRepository = providers.Factory(AccountRepositoryImpl, db=db)
    project_repository: ProjectRepository = providers.Factory(ProjectRepositoryImpl, db=db)
    project_member_repository: ProjectMemberRepository = providers.Factory(ProjectMemberRepositoryImpl, db=db)
    experiment_repository: ExperimentRepository = providers.Factory(ExperimentRepositoryImpl, db=db)

    account_command_usecase: AccountCommandUseCase = providers.Singleton(
        AccountCommandService,
        account_repository=account_repository,
        jwt_token_provider=jwt_token_provider
    )

    project_command_usecase: ProjectCommandUseCase = providers.Singleton(
        ProjectCommandService,
        project_repository=project_repository,
        project_member_repository=project_member_repository
    )

    project_query_usecase: ProjectQueryUseCase = providers.Singleton(
        ProjectQueryService,
        project_repository=project_repository,
    )

    experiment_query_usecase: ExperimentQueryUseCase = providers.Singleton(
        ExperimentQueryService,
        experiment_repository=experiment_repository
    )
