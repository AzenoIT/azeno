from rest_framework import serializers
from . import models


class StudyLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudyLog
        fields = ("user", "study_date", "correct_answer")


class FlashcardStudySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FlashcardStudy
        fields = ("flashcard", )


class DeckStudySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DeckStudy
        fields = ("deck", "study_duration", "realization")
