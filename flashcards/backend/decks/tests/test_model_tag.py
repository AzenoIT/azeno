from decks.models import Tag


def test_tag_gui_representation():
    tag = Tag(name="testTag")

    assert str(tag) == "testTag"


def test_tag_in_db(db):
    tag = Tag(name="testTag2", description="testDescription")
    tag.save()

    assert tag.name == "testTag2"
    assert tag.description == "testDescription"
