def test_comment_gui_representation(comment, remove_test_data):
    assert str(comment) == f"{comment.created_at} - {comment.user} " f"- {comment.deck} - {comment.flashcard}"


def test_comment_creation(comment, flashcard, deck, remove_test_data):
    assert comment.user.username == "test_username"
    assert comment.flashcard == flashcard
    assert comment.deck == deck
    assert comment.comment == "This is a test comment."


def test_comment_fields(comment, remove_test_data):
    assert [*vars(comment)] == [
        "_state",
        "id",
        "user_id",
        "flashcard_id",
        "deck_id",
        "comment",
        "created_at",
        "updated_at",
    ]
