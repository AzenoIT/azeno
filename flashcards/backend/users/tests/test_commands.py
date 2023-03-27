import os
import sys
from io import StringIO

import pytest
from django.core.management import call_command
from django.test import override_settings


@override_settings(DEBUG=True)
@pytest.mark.django_db
def test_create_test_data_command_returns_success_message_when_debug_true(settings, db):
    out = StringIO()
    sys.stdout = out
    call_command(
        "create_test_data",
        "5",
    )
    assert out.getvalue() == "Creating test data\n"


@override_settings(DEBUG=False)
@pytest.mark.django_db
def test_create_test_data_returns_warning_message_when_debug_false(settings, db):
    out = StringIO()
    sys.stdout = out
    call_command(
        "create_test_data",
        "1",
    )
    assert (
        out.getvalue() == "!!! Generating test data is not possible, "
        "because DEBUG is set to False which may indicate production environment!!!\n"
    )


@override_settings(DEBUG=True)
@pytest.mark.django_db
def test_delete_test_data_command_returns_success_message_when_debug_true(
    settings, generated_data_with_custom_command, db
):
    out = StringIO()
    sys.stdout = out
    call_command("delete_test_data")

    assert out.getvalue() == "Deleting test data\n"


@override_settings(DEBUG=True)
@pytest.mark.django_db
def test_delete_data_command_deletes_only_non_admin_users(
    settings, generated_data_with_custom_command, db, django_user_model
):
    database_before_calling_command = django_user_model.objects.all().count()
    call_command("delete_test_data")
    superuser = django_user_model.objects.get(email=os.environ.get("DJ_SU_EMAIL"))

    assert database_before_calling_command == 6
    assert superuser.email == os.environ.get("DJ_SU_EMAIL")


@override_settings(DEBUG=False)
@pytest.mark.django_db
def test_delete_test_data_command_returns_warning_message_when_debug_false(
    settings, generated_data_with_custom_command, db
):
    out = StringIO()
    sys.stdout = out
    call_command("delete_test_data")

    assert (
        out.getvalue() == "!!!Deleting data is not possible, because DEBUG is set to False, "
        "which may indicate production environment!!!\n"
    )
