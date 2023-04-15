from datetime import date


def test_correct_gui_representation(flashcard, remove_test_data):
    assert str(flashcard) == "test"


def test_flashcard_creation(deck, remove_test_data, user, difficulty, flashcard, category):
    assert flashcard.deck == deck.pk
    assert flashcard.category == category.pk
    assert flashcard.rating_flashcard == 1
    assert flashcard.question == "test"
    assert flashcard.answer == "test"
    assert isinstance(flashcard.date_modification, date)
    assert flashcard.author == user.id
    assert flashcard.difficulty == difficulty.pk


def test_flashcard_fields(flashcard, remove_test_data):
    assert [*vars(flashcard)] == [
        "_state",
        "id",
        "deck",
        "category",
        "rating_flashcard",
        "is_active",
        "question",
        "answer",
        "date_added",
        "date_modification",
        "author",
        "difficulty",
    ]
