import pytest

from django.core.management import call_command
from django.test import override_settings
from newsletters.models import Agreements


@pytest.fixture
@override_settings(DEBUG=True)
def generated_data_with_custom_command(settings, db):
    """Fixture for calling create_test_data command

    :return func call_command: call_command
    """
    return call_command(
        "create_test_data",
        "5",
    )


@pytest.fixture
def newsletter(db):
    return Agreements.objects.create(email="test_fixture_newsletter@newsletters.com", checkbox_1=True)
