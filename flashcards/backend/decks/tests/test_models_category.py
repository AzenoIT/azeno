import pytest
from django.db import IntegrityError, DataError

from ..models import Category


def test_category_gui_representation():
    category = Category(name="test category", description="test category description")

    assert str(category) == category.name


def test_category_name_max_length(category):
    with pytest.raises(DataError) as excinfo:
        Category.objects.create(name="test category too long name", description="")

    assert "value too long for type character varying(24)" in str(excinfo.value)


def test_category_in_db(category):
    assert category.name == "test category"
    assert category.description == "test category description"


def test_category_name_uniqueness(category):
    name = category.name

    with pytest.raises(IntegrityError) as excinfo:
        Category.objects.create(name=name, description="")

    assert "duplicate key value violates unique constraint" in str(excinfo.value)
