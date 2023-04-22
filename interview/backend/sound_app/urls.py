from django.urls import path
from . import views

urlpatterns = [
    path('record/', views.record_view, name='record'),
    path('play/<str:filename>/', views.play_view, name='play'),
]
