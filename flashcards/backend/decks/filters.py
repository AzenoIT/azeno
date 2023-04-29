from django_filters import rest_framework as filters

from decks.models import Deck


class DeckFilter(filters.FilterSet):
    pass


class TagFilter(filters.FilterSet):
    pass


class CategoryFilter(filters.FilterSet):
    pass


class DifficultyLevelFilter(filters.FilterSet):
    pass


class FlashcardFilter(filters.FilterSet):
    pass
