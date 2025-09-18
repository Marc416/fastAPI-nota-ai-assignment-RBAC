from pydantic import BaseModel

from rbac.domain.experiment.entity.experiment import Experiment


class ExperimentRetriveAllResponse(BaseModel):
    id: int
    experiment_id: str
    title: str

    @classmethod
    def of(cls, experiment: Experiment) -> "ExperimentRetriveAllResponse":
        return ExperimentRetriveAllResponse(
            id=experiment.id,
            experiment_id=experiment.experiment_id,
            title=experiment.title
        )