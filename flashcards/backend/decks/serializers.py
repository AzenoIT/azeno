from rest_framework import serializers

from decks.models import Deck, Category, DifficultyLevel


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "description")


class DifficultyLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DifficultyLevel
        fields = ("id", "name", "value")


class DeckSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    difficulty_level = DifficultyLevelSerializer()

    class Meta:
        model = Deck
        fields = (
            "id",
            "name",
            "author",
            "price",
            "category",
            "difficulty_level",
            "popularity",
            "rating",
            "is_public",
            "is_active",
            "description",
            "image",
        )
