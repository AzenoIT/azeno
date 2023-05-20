import pytest
from django.db import IntegrityError

from ..models import Tag


def test_tag_gui_representation():
    tag = Tag(name="test_tag")

    assert str(tag) == "test_tag"


def test_tag_in_db(tag_db):
    assert tag_db.name == "tag_2"


def test_tag_unique_name_regardless_of_he_case_used_in_db(tag_db):
    with pytest.raises(IntegrityError) as excinfo:
        Tag.objects.create(name="TaG_2")
        tag_db.full_clean()
        tag_db.save()

    assert 'duplicate key value violates unique constraint "unique_lower_name_tag"' in str(excinfo.value)


def test_add_tag_to_deck(deck, flashcard):
    tag = Tag.objects.create(name="tag_3")
    tag.flashcards.add(flashcard)
    deck.tags.add(tag)

    assert deck.tags.count() == 1
    assert deck.tags.first() == tag


def test_add_tag_to_flashcard(deck, flashcard):
    tag = Tag.objects.create(name="tag_3")
    tag.decks.add(deck)
    flashcard.tags.add(tag)

    assert flashcard.tags.count() == 1
    assert flashcard.tags.first() == tag
