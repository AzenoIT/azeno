from rest_framework import routers

from .viewsets import DeckViewSet

app_name = "decks"

router = routers.DefaultRouter()
router.register(r"decks", DeckViewSet, basename="deck")

urlpatterns = [*router.urls]
