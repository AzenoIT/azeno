from datetime import timedelta

from players.models import AccountType, Player


def test_account_type_representation_in_gui():
    account_type = AccountType(name="Plus", duration=timedelta(days=60), cost=10)
    assert str(account_type) == "Plus"


def test_account_type_creation(account_type):
    account_types = AccountType.objects.all()
    assert account_type in account_types


def test_player_represetation_in_gui(account_type):
    player = Player(nick="mati", account_type=account_type)
    assert str(player) == "mati"


def test_player_creation(account_type):
    player = Player.objects.create(nick="mati", account_type=account_type)
    players = Player.objects.all()
    assert player in players
