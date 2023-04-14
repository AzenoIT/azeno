import pytest
from django.db import IntegrityError

from ..models import Tag


def test_tag_gui_representation():
    tag = Tag(name="test_tag")

    assert str(tag) == "test_tag"


def test_tag_in_db(tag_db):
    assert tag_db.name == "tag_2"


def test_tag_unique_name_regardless_of_he_case_used_in_db(tag_db, flashcard, deck):
    with pytest.raises(IntegrityError) as excinfo:
        Tag.objects.create(name="TaG_2", flashcard=flashcard, deck=deck)
        tag_db.full_clean()
        tag_db.save()

    assert 'duplicate key value violates unique constraint "unique_lower_name_tag"' in str(excinfo.value)
