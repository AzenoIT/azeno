from ..models import DifficultyLevel


def test_difficulty_level_gui_representation():
    difficulty_level = DifficultyLevel(name="hard", value=1)
    assert str(difficulty_level) == difficulty_level.name


def test_difficulty_level_in_db(difficulty_level):
    assert DifficultyLevel.objects.count() == 1
    assert DifficultyLevel.objects.first().name == difficulty_level.name


def test_difficulty_level_meta_information():
    assert DifficultyLevel._meta.get_field("name").max_length == 20
    assert DifficultyLevel._meta.get_field("name").unique is True
    assert DifficultyLevel._meta.get_field("value").unique is True
    assert DifficultyLevel._meta.verbose_name == "difficulty level"
    assert DifficultyLevel._meta.verbose_name_plural == "difficulty level`s"


def test_difficulty_level_custom_save(db, difficulty_level):
    """Test will check that names which are exact but lover or upper case,
    will not be added to DB, and existing record will be returned
    """

    difficulty_level_2 = DifficultyLevel.objects.create(name=difficulty_level.name.lower(), value=2)

    assert difficulty_level_2.name == difficulty_level.name
