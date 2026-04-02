from django.db.models.query import QuerySet
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Workout
from .permissions import IsWorkoutOwner
from .serializers import WorkoutSerializer


class CreateWorkoutView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = WorkoutSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ListWorkoutView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = WorkoutSerializer

    def get_queryset(self) -> QuerySet:
        return Workout.objects.filter(user=self.request.user.pk).prefetch_related()


class RetrieveWorkout(RetrieveAPIView):
    permission_classes = (
        IsAuthenticated,
        IsWorkoutOwner,
    )
    serializer_class = WorkoutSerializer
    lookup_field = "id"
    queryset = Workout.objects.all()
