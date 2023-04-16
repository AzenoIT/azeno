from datetime import datetime


def test_correct_gui_representation(flashcard_study, remove_test_data):
    flashcard_study_ = flashcard_study
    assert str(flashcard_study_) == f"{flashcard_study_.study_date} - {flashcard_study_.flashcard} " \
                                    f"- {flashcard_study_.user} - {flashcard_study_.correct_answers} correct answers"


def test_flashcard_study_creation(flashcard_study, flashcard, remove_test_data):
    assert flashcard_study.user.username == "test_username"
    assert flashcard_study.correct_answers == 2
    assert flashcard_study.flashcard == flashcard
    assert isinstance(flashcard_study.study_date, datetime)


def test_flashcard_study_fields(flashcard_study, remove_test_data):
    assert [*vars(flashcard_study)] == [
        "_state",
        "id",
        "user_id",
        "study_date",
        "correct_answers",
        "flashcard_id",
    ]
