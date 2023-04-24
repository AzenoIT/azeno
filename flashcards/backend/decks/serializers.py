from rest_framework import serializers

from .models import Deck, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "description")


class DeckSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Deck

        fields = (
            "id",
            "name",
            "author",
            "price",
            "category",
            "popularity",
            "rating",
            "is_public",
            "is_active",
            "description",
            "image",
        )
