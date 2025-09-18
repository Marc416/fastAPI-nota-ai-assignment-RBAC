from datetime import datetime

from pydantic import UUID4
from sqlalchemy import Integer, Column, String, DateTime, Enum as SAEnum

from rbac.application.config.db.base import Base

class Experiment(Base):
    __tablename__ = "experiment"

    id = Column(Integer, primary_key=True, autoincrement=True)
    experiment_id = Column(String(36), unique=True, nullable=False)
    title = Column(String(255), nullable=False)



