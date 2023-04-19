from django.shortcuts import render
from rest_framework import generics

from . import serializers, models


class BadgeRetrieveView(generics.RetrieveAPIView):
    """Retrieve a single Badge instance by its primary key.

    .. attention::
        * For now authentication is not required.

    :ivar queryset: The queryset used to retrieve the :class:`stats.models.Badge` instance.
    :vartype queryset: QuerySet
    :ivar serializer_class: The serializer class used to serialize Badge data.
    :vartype serializer_class: Type[serializers.BadgeSerializer]

    """

    queryset = models.Badge.objects.all()
    serializer_class = serializers.BadgeSerializer


class BadgeListView(generics.ListAPIView):
    """List all Badge instances.

    .. attention::
        * For now authentication is not required.

    :ivar queryset: The queryset used to retrieve all :class:`stats.models.Badge` instances
    :vartype queryset: Queryset
    :ivar serializer_class: The serializer class used for serializing Badge data.
    :vartype serializer_class: Type[serializers.BadgeSerializer]

    """

    queryset = models.Badge.objects.all()
    serializer_class = serializers.BadgeSerializer
