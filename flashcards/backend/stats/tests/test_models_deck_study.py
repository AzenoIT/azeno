from datetime import datetime

from _datetime import timedelta
from _decimal import Decimal


def test_correct_gui_representation(deck_study, remove_test_data):
    deck_study_ = deck_study
    assert (
        str(deck_study_) == f"{deck_study_.study_date} - {deck_study_.deck} "
        f"- {deck_study_.user} - {deck_study_.realization}%"
    )


def test_deck_study_creation(deck_study, deck, remove_test_data):
    assert deck_study.user.username == "test_username"
    assert deck_study.correct_answers == 3
    assert deck_study.deck == deck
    assert deck_study.realization == Decimal(42)
    assert isinstance(deck_study.realization, Decimal)
    assert isinstance(deck_study.study_date, datetime)
    assert isinstance(deck_study.study_duration, timedelta)


def test_deck_study_fields(deck_study, remove_test_data):
    assert [*vars(deck_study)] == [
        "_state",
        "id",
        "user_id",
        "study_date",
        "correct_answers",
        "deck_id",
        "study_duration",
        "realization",
    ]
