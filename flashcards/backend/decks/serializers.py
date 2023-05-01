from rest_framework import serializers

from .models import Category, Tag, Deck, DifficultyLevel


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Category model.

    :returns: CategorySerializer
    :rtype: rest_framework.serializers.Serializer

    """

    class Meta:
        model = Category
        fields = ("id", "image", "name", "description")


class TagSerializer(serializers.ModelSerializer):
    """Serializer for Tag model.

    :returns: TagSerializer
    :rtype: rest_framework.serializers.Serializer

    """

    class Meta:
        model = Tag
        fields = ("id", "name", "deck_id", "flashcard_id")


class DifficultyLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DifficultyLevel
        fields = ("id", "name", "value")


class DeckSerializer(serializers.ModelSerializer):
    """Serializer for Deck model.

    :returns: DeckSerializer
    :rtype: rest_framework.serializers.Serializer

    """

    category = CategorySerializer()
    difficulty_level = DifficultyLevelSerializer()

    class Meta:
        model = Deck
        fields = (
            "id",
            "image",
            "name",
            "category",
            "difficulty_level",
            "is_public",
            "price",
            "author",
            "popularity",
            "rating",
            "description",
        )


class AddDeckWithCategorySerializer(serializers.ModelSerializer):
    """Serializer for creating deck with category.

    :returns: AddDeckWithCategorySerializer
    :rtype: rest_framework.serializers.Serializer

    """

    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    image = serializers.FileField(default=None, required=False)

    class Meta:
        model = Deck
        fields = (
            "id",
            "image",
            "name",
            "category",
            "difficulty_level",
            "category_id",
            "is_public",
            "price",
            "popularity",
            "rating",
            "description",
        )

    @staticmethod
    def create(validated_data):
        deck = Deck.objects.create(**validated_data)

        return deck
