import pytest
from fastapi.testclient import TestClient

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from fast_zero.models import Base
from fast_zero.app import app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    yield Session()
    Base.metadata.drop_all(engine)
