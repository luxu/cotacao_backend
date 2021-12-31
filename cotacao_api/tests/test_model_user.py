import pytest
from django.contrib.auth.models import User
from model_bakery import baker


@pytest.fixture
def user(db):
    return baker.make(User, username="marinaul", password="2")


@pytest.fixture
def users(db):
    return baker.make(User, 3)


@pytest.fixture
def resp(client, db):
    return client.get("/")


def test_should_username(user) -> None:
    assert user.password is not None
    assert user.username is not None
