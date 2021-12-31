import datetime

import pytest
from django.urls import reverse
from model_mommy import mommy

from payments.models import Payments


@pytest.fixture
@pytest.mark.usefixtures("providers")
def payments(providers):
    for provider in providers:
        payments = Payments(
            provider=provider,
            due_date=datetime.datetime(2020, 10, 10, 12, 56, 54, 324893),
            original_value=1200
            # issue_date = datetime.datetime.date('2021-09-28'),
            # advance_date =
            # decision =
            # discount_value =
            # value_new =
        )
        payments.save()
    return Payments.objects.all()


@pytest.fixture
@pytest.mark.usefixtures("providers")
def payment(providers):
    return mommy.make(
        Payments,
        provider=providers[0],
        due_date=datetime.datetime(2020, 7, 10, 12, 56, 54, 324893)
    )


@pytest.fixture
def list_payments(client, db):
    resp = client.get(reverse('list_payments'))
    return resp


def test_list_payments(payments):
    assert payments is not None


def test_fields_payments(payment):
    assert payment.decision == 0
    assert payment.due_date == datetime.datetime(2020, 7, 11, 12, 56, 54, 324893)


def test_acessar_um_link_e_não_conseguir_logar(list_payments):
    assert list_payments.status_code == 302
