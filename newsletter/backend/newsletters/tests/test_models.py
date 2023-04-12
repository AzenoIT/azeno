from newsletters.models import Agreements


def test_representation_in_gui():
    user_agreement = Agreements(email="test@newsletters.com")

    assert str(user_agreement) == "test@newsletters.com"


def test_newsletter_creation(newsletter):
    agreement = Agreements.objects.get(email="test_fixture_newsletter@newsletters.com")

    assert agreement.checkbox_1
    assert agreement.checkbox_2 is False
    assert agreement.checkbox_3 is False
