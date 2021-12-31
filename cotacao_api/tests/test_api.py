import pytest
from django.urls import reverse

from moeda.models import Moeda


@pytest.fixture
def moeda(db):
    m1 = Moeda(initials="BRL", name_coin="Real", data="2021-12-29", value="5.646642484296204")
    m1.save()
    m2 = Moeda(initials="JPY", name_coin="Iene", data="2021-12-29", value="114.98717154737679")
    m2.save()
    m3 = Moeda(initials="EUR", name_coin="Euro", data="2021-12-29", value="0.8847208705653365")
    m3.save()
    return m1


def test_listar_todos_dados(client, moeda):
    resp = client.get(reverse('api_cotacoes'))
    assert len(resp.json()) == 3
