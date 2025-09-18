from abc import ABC, abstractmethod
from typing import List

from rbac.domain.experiment.dto.response.experiment_retrive_all_response import ExperimentRetriveAllResponse
from rbac.domain.project.dto.request.member_request import MemberRequest
from rbac.domain.project.dto.response.project_response import ProjectResponse
from rbac.domain.experiment.entity.experiment import Experiment


class ExperimentQueryUseCase(ABC):
    @abstractmethod
    def retrieve_all_experiments(self) -> List[ExperimentRetriveAllResponse]:
        raise NotImplementedError()
