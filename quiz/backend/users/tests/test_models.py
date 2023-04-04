import pytest
from django.core.exceptions import ValidationError


@pytest.mark.django_db
def test_create_user(django_user_model):
    user = django_user_model.objects.create_user(
        email="testuser@test.com",
        username="testUser",
        password="testPass123",
    )
    saved_user = django_user_model.objects.get(email="testuser@test.com")

    assert saved_user.username == "testUser"


@pytest.mark.django_db
def test_create_user_raises_value_error_when_email_is_empty_string(
    django_user_model, db
):
    with pytest.raises(ValueError) as excinfo:
        user = django_user_model.objects.create_user(
            username="testUser",
            email="",
            password="testPass123",
        )

        assert "Email field is required" in str(excinfo.value)


@pytest.mark.django_db
def test_create_user_without_username(django_user_model, db):
    django_user_model.objects.create_user(
        email="testuser@mail.com",
        password="testPass123",
    )

    saved_user = django_user_model.objects.get(email="testuser@mail.com")

    assert saved_user.email == "testuser@mail.com"


@pytest.mark.django_db
def test_create_superuser(django_user_model, db):
    django_user_model.objects.create_superuser(
        email="testsuper@user.com",
        username="testSuperUser",
        password="testPass123",
    )

    saved_superuser = django_user_model.objects.get(email="testsuper@user.com")

    assert saved_superuser.is_superuser == True


def test_custom_user_object_representation_in_gui(django_user_model):
    user = django_user_model(
        email="testuser@test.com",
        username="testUser",
        password="testPass123",
    )
    assert str(user) == "testuser@test.com"


@pytest.mark.parametrize(
    "username",
    [
        "analyticalMonkey",
        "assertivePesto",
        "vibrantArrow",
    ],
)
def test_custom_user_validates_non_profane_username(username, django_user_model, db):
    django_user_model.objects.create_user(
        email=f"{username}@testmail.com", username=username, password="testPass123"
    )
    saved_user = django_user_model.objects.get(email=f"{username}@testmail.com")
    assert saved_user.username == username


@pytest.mark.parametrize(
    "username",
    [
        "fuckinMonkey",
        "cuntFace",
        "boobs_rock",
        "JP2-kocha-dzieci",
    ],
)
def test_custom_user_raises_error_when_profane_username(
    username, django_user_model, db
):
    with pytest.raises(ValidationError) as excinfo:
        django_user_model.objects.create_user(
            username=username, email="test@mail.com", password="testPass123"
        )
    assert "This name contains profane word:" in str(excinfo.value)
