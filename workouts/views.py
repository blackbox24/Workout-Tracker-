from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import WorkoutSerializer


class CreateWorkoutView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = WorkoutSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
