from typing import List

from rbac.domain.experiment.dto.response.experiment_retrive_all_response import ExperimentRetriveAllResponse
from rbac.domain.experiment.repository.experiment_repository import ExperimentRepository
from rbac.domain.experiment.usecase.experiment_query_usecase import ExperimentQueryUseCase


class ExperimentQueryService(ExperimentQueryUseCase):
    def __init__(self,
                 experiment_repository: ExperimentRepository):
        self.experiment_repository = experiment_repository

    def retrieve_all_experiments(self) -> List[ExperimentRetriveAllResponse]:
        return [ExperimentRetriveAllResponse.of(experiment=experiment)
                    for experiment in self.experiment_repository.get_all()]