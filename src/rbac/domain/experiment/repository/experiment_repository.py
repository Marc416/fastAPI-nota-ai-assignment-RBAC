from abc import ABC, abstractmethod
from typing import Optional, List
from rbac.domain.experiment.entity.experiment import Experiment


class ExperimentRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Experiment]:
        raise NotImplementedError()