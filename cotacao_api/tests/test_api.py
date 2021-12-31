import pytest
from requests import get

from django.urls import reverse

from pagseguro.settings import BASE_URL


@pytest.fixture
def url_api_request_advance():
    url_view = reverse('api_request_advance', kwargs={'payment_id': '6'})
    url = ''.join((BASE_URL, url_view))
    return url


@pytest.fixture
def url_api_payment_id():
    url_view = reverse('api_request_advance', kwargs={'payment_id': '4'})
    url = ''.join((BASE_URL, url_view))
    return url


def test_solicitar_antecipacao_de_recebivel(url_api_request_advance):
    headers = {'Authorization': 'Basic bWFyaW5hdWw6Mg=='}
    resp = get(url_api_request_advance, headers=headers)
    assert resp.status_code == 200


def test_listar_por_estado_de_pagamento(url_api_payment_id):
    headers = {'Authorization': 'Basic bWFyaW5hdWw6Mg=='}
    res = get(url_api_payment_id, headers=headers)
    assert res.status_code == 200
