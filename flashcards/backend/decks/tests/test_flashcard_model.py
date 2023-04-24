from datetime import date
from django.contrib.contenttypes.models import ContentType


def test_correct_gui_representation(flashcard, remove_test_data):
    assert str(flashcard) == "test"


def test_flashcard_creation(deck, remove_test_data, user, difficulty, flashcard, category, text):
    assert flashcard.deck == deck.pk
    assert flashcard.category == category.pk
    assert flashcard.rating_flashcard == 1
    assert flashcard.content_type_question == ContentType.objects.get_for_model(text.pk)
    assert flashcard.object_id_question == 1
    assert flashcard.content_type_answer == ContentType.objects.get_for_model(text.pk)
    assert flashcard.object_id_answer == 1
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
        "content_type_question",
        "object_id_question",
        "content_type_answer",
        "object_id_answer",
        "date_added",
        "date_modification",
        "author",
        "difficulty",
    ]
