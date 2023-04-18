from django.urls import path

from . import views

app_name = "stats"

urlpatterns = [
    path("badges/<int:pk>/", views.BadgeRetrieveView.as_view(), name="badge_detail"),
]
