from fastapi import FastAPI
import logging

from rbac.application.config.container import Container
from rbac.application.config.db.database import engine

logger = logging.getLogger(__name__)

def lifespan(app: FastAPI):
    container = Container()
    container.wire()
    app.container = container

    # FastAPI 인스턴스 기동시 필요한 작업 수행.
    logger.info("Starting up...")
    yield

    #FastAPI 인스턴스 종료시 필요한 작업 수행
    logger.info("Shutting down...")
    engine.dispose()