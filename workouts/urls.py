from django.urls import path

from . import views

urlpatterns = [
    path("", views.ListCreateWorkoutView.as_view(), name="list_create_workout_view"),
    path(
        "<int:id>/", views.RetrieveWorkoutView.as_view(), name="retrieve_update_delete_workout_view"
    ),
]
