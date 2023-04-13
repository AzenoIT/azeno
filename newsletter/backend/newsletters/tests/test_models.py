from newsletters.models import Agreements


def test_agreements_gui_representation():
    user_agreement = Agreements(email="test@newsletters.com")

    assert str(user_agreement) == "test@newsletters.com"
