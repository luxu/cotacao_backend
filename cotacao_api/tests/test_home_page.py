import pytest

from pagseguro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    resp = client.get('/')
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<title>Administradora PAGSEGURO</title>')
