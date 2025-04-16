import os

import pytest
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker

from rbac.application.config.db.database import get_db
from rbac.main import app

# 같은 DATABASE_CONN 사용해도 되고 별도로 테스트용 설정해도 됨
DATABASE_URL = os.getenv("DATABASE_CONN")

# 테스트용 엔진 & 세션
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

@pytest.fixture(scope="function")
def db_session():
    """각 테스트마다 독립된 트랜잭션 제공"""
    connection = engine.connect()
    transaction = connection.begin()  # 트랜잭션 시작
    session = TestingSessionLocal(bind=connection)

    # SAVEPOINT 생성
    nested_transaction = connection.begin_nested()

    # 세션 이벤트 리스너로 SAVEPOINT 관리
    @event.listens_for(session, "after_transaction_end")
    def restart_savepoint(session, transaction):
        nonlocal nested_transaction
        if transaction.nested and not transaction._parent.nested:
            nested_transaction.rollback()  # 롤백 후 새로운 nested 트랜잭션 시작
            nested_transaction = connection.begin_nested()

    try:
        yield session  # db_session을 테스트에서 사용하도록 yield
        if session.is_active:
            session.commit()  # 명시적 커밋
    finally:
        # 세션 종료 및 트랜잭션 롤백
        session.close()
        if transaction.is_active:
            transaction.rollback()  # 트랜잭션 롤백 <- 롤백에 안돼서 테스트 코드 작성 우선 중단
        connection.close()

@pytest.fixture(scope="function")
def client(db_session):
    """의존성 주입을 통해 db_session으로 대체"""
    def override_get_db():
        try:
            yield db_session  # db_session을 반환
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db  # 의존성 주입

    from fastapi.testclient import TestClient
    with TestClient(app) as test_client:
        yield test_client  # 테스트 클라이언트 반환