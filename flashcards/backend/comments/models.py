from django.contrib.auth import get_user_model
from django.db import models


class Comment(models.Model):
    """Model for representing user's comments in response to flashcards and decks

    :param user: related user object
    :type user: CustomUser
    :param flashcard: related flashcard object
    :type flashcard: Flashcard
    :param deck: related deck object
    :type deck: Deck
    :param description: contents of a comment
    :type description: text
    """
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="comments")
    flashcard = models.ForeignKey("decks.Flashcard", on_delete=models.CASCADE, related_name="comments")
    deck = models.ForeignKey("decks.Deck", on_delete=models.CASCADE, related_name="comments")
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.created_at} - {self.user} - {self.deck} - {self.flashcard}'
