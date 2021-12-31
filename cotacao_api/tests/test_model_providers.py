import pytest

from providers.models import Providers
from faker import Faker
from model_mommy import mommy


@pytest.fixture
@pytest.mark.usefixtures("users")
def providers(users):
    fake = Faker()
    for user in users:
        provider = Providers(user=user, corporate_name=fake.first_name(), cnpj="233443230000130")
        provider.save()
    return Providers.objects.all()


@pytest.fixture
def provider_corporate_name(db):
    provider = mommy.make(
        Providers,
        corporate_name="Holowiwi"
    )
    return provider


def test_list_providers(providers):
    assert providers != []


def test_corporate_name(providers):
    for provider in providers:
        assert provider.corporate_name is not None


def test_provider_with_corporate_name(provider_corporate_name):
    assert provider_corporate_name.corporate_name == 'Holowiwi'
