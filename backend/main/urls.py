from django.urls import path
from .views import RunDetectionView

urlpatterns = [
    path("run_detection/", RunDetectionView.as_view()),
]
