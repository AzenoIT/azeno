from rest_framework.routers import DefaultRouter

from . import viewsets

app_name = "decks"

router = DefaultRouter()
router.register(r"decks", viewsets.DeckViewSet, basename="deck")

urlpatterns = [*router.urls]
