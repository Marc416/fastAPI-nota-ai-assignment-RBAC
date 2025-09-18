from typing import List

from dependency_injector.wiring import inject, Provide
from sqlalchemy.orm import Session

from rbac.domain.experiment.entity.experiment import Experiment
from rbac.domain.experiment.repository.experiment_repository import ExperimentRepository


class ExperimentRepositoryImpl(ExperimentRepository):

    @inject
    def __init__(self, db: Session = Provide["db"]):
        self.db = db


    def get_all(self) -> list[type[Experiment]]:
        return self.db.query(Experiment).all()


