from django.shortcuts import render
from rest_framework import generics

from . import serializers, models


class BadgeRetrieveView(generics.RetrieveAPIView):
    queryset = models.Badge.objects.all()
    serializer_class = serializers.BadgeSerializer


class BadgeListView(generics.ListAPIView):
    queryset = models.Badge.objects.all()
    serializer_class = serializers.BadgeSerializer
