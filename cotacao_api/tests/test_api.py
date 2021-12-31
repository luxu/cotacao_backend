import pytest

from django.urls import reverse


@pytest.fixture
def url_que_carrega_os_dados(client, db):
    """Criado o banco, roda as migrations, acessa a url externa e alimenta o banco com os dados"""
    return client.get(reverse("api_site"))


def test_carregar_dados_api_externa(url_que_carrega_os_dados):
    assert url_que_carrega_os_dados.status_code == 200


def test_base_de_dados_vazi(client, db):
    resp = client.get(reverse('api_cotacoes'))
    assert len(resp.json()) == 0


def test_listar_todos_dados(client, url_que_carrega_os_dados):
    resp = client.get(reverse('api_cotacoes'))
    assert len(resp.json()) > 0
