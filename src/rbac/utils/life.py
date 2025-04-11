from fastapi import FastAPI

from rbac.config.container import Container
from rbac.config.db.database import engine

def lifespan(app: FastAPI):
    container = Container()
    container.wire()
    app.container = container

    # FastAPI 인스턴스 기동시 필요한 작업 수행.
    print("Starting up...")
    yield

    #FastAPI 인스턴스 종료시 필요한 작업 수행
    print("Shutting down...")
    engine.dispose()