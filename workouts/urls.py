from django.urls import path

from . import views

urlpatterns = [
    path("", views.ListCreateWorkoutView.as_view(), name="list_create_workout_view"),
    path(
        "<int:id>/", views.RetrieveWorkoutView.as_view(), name="retrieve_update_delete_workout_view"
    ),
    path(
        "<int:id>/schedule",
        views.UpdateScheduleWorkoutView.as_view(),
        name="update_workout_schedule_view",
    ),
    path("<int:id>/comments/", views.CommentWorkoutView.as_view(), name="comment_workout_view"),
]
