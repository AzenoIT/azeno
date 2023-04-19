from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, status

from .models import Deck
from .serializers import DeckSerializer


class DeckViewSet(viewsets.ModelViewSet):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer

    def list(self, request, *args, **kwargs):
        decks = self.serializer_class(self.get_queryset().order_by("-rating"), many=True)
        return Response(data=decks.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, pk=None, **kwargs):
        deck = get_object_or_404(queryset=self.get_queryset(), pk=pk)
        return Response(data=self.serializer_class(deck).data, status=status.HTTP_200_OK)
