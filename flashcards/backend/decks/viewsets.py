from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, status
from django_filters import rest_framework as filters

from .filters import DeckFilter
from .models import Deck
from .serializers import DeckSerializer


class DeckViewSet(viewsets.ModelViewSet):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = DeckFilter
    filterset_fields = [
        "category__name",
        "difficulty_level__name",
        "difficulty_level__value",
        "name",
        "price",
        "popularity",
        "rating",
    ]

    def list(self, request, *args, **kwargs):
        self.queryset = self.filter_queryset(self.get_queryset().order_by("-rating"))
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, pk=None, **kwargs):
        deck = get_object_or_404(queryset=self.get_queryset(), pk=pk)
        return Response(data=self.serializer_class(deck).data, status=status.HTTP_200_OK)
