from rest_framework import generics

from . import models, serializers


class StudyLogListAPIView(generics.ListAPIView):
    queryset = models.StudyLog.objects.all()
    serializer_class = serializers.StudyLogSerializer


class FlashcardStudyRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.FlashcardStudy.objects.all()
    serializer_class = serializers.FlashcardStudySerializer

class FlashcardStudyListAPIView(generics.ListAPIView):
    queryset = models.FlashcardStudy.objects.all()
    serializer_class = serializers.FlashcardStudySerializer


class DeckStudyRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.DeckStudy.objects.all()
    serializer_class = serializers.DeckStudySerializer

class DeckStudyListAPIView(generics.ListAPIView):
    queryset = models.DeckStudy.objects.all()
    serializer_class = serializers.DeckStudySerializer
