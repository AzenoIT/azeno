from players.models import Player


def test_player_representation_in_gui(account_type):
    player = Player(nick="mati", account_type=account_type)
    assert str(player) == "mati"


def test_player_creation(account_type):
    player = Player.objects.create(nick="mati", account_type=account_type)
    players = Player.objects.all()
    assert player in players
