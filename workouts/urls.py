from django.urls import path

from . import views

urlpatterns = [
    path("", views.CreateWorkoutView.as_view(), name="create_workout_view"),
]
