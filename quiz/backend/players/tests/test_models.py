from players.models import Player


def test_object_representation_in_gui():
    player = Player(nick="testPlayer")

    assert str(player) == "testPlayer"


def test_bot_creation(player_bot):
    players = Player.objects.all()
    assert player_bot in players
