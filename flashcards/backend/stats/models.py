from django.contrib.auth import get_user_model
from django.db import models


class StudyLog(models.Model):
    """Abstract model for tracking user's study progress.

    Inherits only from Model class.

    :param user: related user object
    :type user: User
    :param correct_answers: correct answers count
    :type correct_answers: int
    """

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="%(class)ss")
    study_date = models.DateTimeField(auto_now_add=True)
    correct_answers = models.PositiveIntegerField(verbose_name="Correct answers count")

    class Meta:
        abstract = True


class FlashcardStudy(StudyLog):
    """Model for acquisition of data regarding flashcard study

    :param flashcard: studied flashcard
    :type flashcard: Flashcard
    """

    flashcard = models.ForeignKey("decks.Flashcard", on_delete=models.CASCADE, related_name="study_logs")

    def __str__(self):
        return f"{self.study_date} - {self.flashcard} - {self.user} - {self.correct_answers} correct answers"


class DeckStudy(StudyLog):
    """Model for acquisition of data regarding deck study

    :param deck: studied deck name
    :type deck: Deck
    :param study_duration: duration of a deck study session
    :type study_duration: timedelta
    :param realization: deck realization percentage
    :type realization: Decimal
    """

    deck = models.ForeignKey("decks.Deck", on_delete=models.CASCADE, related_name="study_logs")
    study_duration = models.DurationField()
    realization = models.DecimalField(max_digits=4, decimal_places=1)

    def __str__(self):
        return f"{self.study_date} - {self.deck} - {self.user} - {self.realization}%"
