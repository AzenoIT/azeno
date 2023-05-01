from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from . import models, serializers
from .models import Category


class DeckViewSet(ModelViewSet):
    queryset = models.Deck.objects.all()
    serializer_class = serializers.DeckSerializer
    parser_classes = [MultiPartParser, JSONParser]

    def retrieve(self, request, *args, pk=None, **kwargs):
        deck = get_object_or_404(queryset=self.get_queryset(), pk=pk)
        return Response(data=self.serializer_class(deck).data, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        self.queryset = self.filter_queryset(self.get_queryset().order_by("-rating"))
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = serializers.AddDeckWithCategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        category_id = serializer.validated_data.pop("category_id")
        category = Category.objects.get(pk=category_id)
        image = serializer.validated_data.get("image", None)

        if not image:
            image = category.image

        deck = serializer.create(
            {**serializer.validated_data, "author": request.user, "category": category, "image": image}
        )

        deck_serializer = serializers.DeckSerializer(deck)

        return Response(deck_serializer.data, status=status.HTTP_201_CREATED)
