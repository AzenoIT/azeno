from django.shortcuts import render
from rest_framework import generics

from . import serializers, models


class BadgeRetrieveView(generics.RetrieveAPIView):
    """Retrieve a single badge instance by its primary key.

    * For now authentication is not required.

    :ivar queryset: The queryset used to retrieve the :class:`stats.models.Badge` instance.
    :type queryset: QuerySet
    :ivar serializer_class: The serializer class used to serialize Badge data.
    :type serializer_class: Type[serializers.BadgeSerializer]

    """

    queryset = models.Badge.objects.all()
    serializer_class = serializers.BadgeSerializer


class BadgeListView(generics.ListAPIView):
    """List all badge instances.

    * For now authentication is not required.

    :ivar queryset: The queryset used to retrieve all :class:`stats.models.Badge` instances
    :type queryset: Queryset
    :ivar serializer_class: The serializer class used for serializing Badge data.
    :type serializer_class: Type[serializers.BadgeSerializer]

    """

    queryset = models.Badge.objects.all()
    serializer_class = serializers.BadgeSerializer
