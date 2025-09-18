from typing import List

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from fastapi_utils.cbv import cbv

from rbac.application.config.container import Container
from rbac.domain.experiment.dto.response.experiment_retrive_all_response import ExperimentRetriveAllResponse
from rbac.domain.experiment.usecase.experiment_query_usecase import ExperimentQueryUseCase

router = APIRouter(prefix="", tags=["experiment-query"])

@cbv(router)
class ExperimentQueryController:
    @inject
    def __init__(
            self,
            experiment_query_usecase: ExperimentQueryUseCase = Depends(Provide[Container.experiment_query_usecase]),
    ):
        self.experiment_query_usecase = experiment_query_usecase


    @router.get("/experiments")
    def get_experiments(self) -> List[ExperimentRetriveAllResponse]:
        return self.experiment_query_usecase.retrieve_all_experiments()