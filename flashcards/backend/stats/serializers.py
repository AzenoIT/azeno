from rest_framework import serializers
from . import models


class StudyLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudyLog
        fields = ('id', 'user', 'study_date', 'correct_answers')

class FlashcardStudySerializer(serializers.ModelSerializer):
    flashcard = serializers.StringRelatedField()
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = models.FlashcardStudy
        fields = ('id', 'user', 'study_date', 'flashcard', 'correct_answers')

class DeckStudySerializer(serializers.ModelSerializer):
    deck = serializers.StringRelatedField()
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = models.DeckStudy
        fields = ('id', 'user', 'study_date', 'deck', 'correct_answers', 'study_duration', 'realization')