from datetime import date

from django.contrib.contenttypes.models import ContentType
from django.utils import timezone


def test_correct_gui_representation(flashcard, remove_test_data):
    assert str(flashcard) == "Test Flashcard"


def test_flashcard_creation(deck, user, remove_test_data, difficulty_level, flashcard, category, text):
    assert flashcard.name == 'Test Flashcard'
    assert flashcard.deck == deck
    assert flashcard.category == category
    assert flashcard.is_active == True
    assert flashcard.rating_flashcard == 1
    assert flashcard.question == text
    assert flashcard.answer == text
    assert flashcard.author == user
    assert flashcard.difficulty == difficulty_level


def test_flashcard_update_date_modification(flashcard, remove_test_data):
    original_date_modification = flashcard.date_modification
    flashcard.rating_flashcard = 5
    flashcard.save()
    assert flashcard.date_modification == original_date_modification


def test_flashcard_update_fields(deck, user, remove_test_data, difficulty_level, flashcard, category, code):
    flashcard.name = 'Updated Flashcard'
    flashcard.rating_flashcard = 3
    flashcard.is_active = False
    flashcard.question = code
    flashcard.answer = code
    flashcard.save()

    assert flashcard.name == 'Updated Flashcard'
    assert flashcard.rating_flashcard == 3
    assert flashcard.is_active == False
    assert flashcard.question == code
    assert flashcard.answer == code
