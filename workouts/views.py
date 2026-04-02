from django.db.models.query import QuerySet
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Workout
from .permissions import IsWorkoutOwner
from .serializers import CommentSerializer, WorkoutSerializer


class ListCreateWorkoutView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = WorkoutSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self) -> QuerySet:
        return Workout.objects.filter(user=self.request.user.pk).prefetch_related()


class RetrieveWorkoutView(RetrieveUpdateDestroyAPIView):
    permission_classes = (
        IsAuthenticated,
        IsWorkoutOwner,
    )
    serializer_class = WorkoutSerializer
    lookup_field = "id"
    queryset = Workout.objects.all()


class CommentWorkoutView(APIView):
    permission_classes = (IsAuthenticated, IsWorkoutOwner)
    serializer_class = CommentSerializer

    # def get(self, request, id=None, *args, **kwargs) -> Response:
    #     comments = Comments.objects.filter(user_id=self.request.user.pk)
    #     if id:
    #         try:
    #             comment = comments.get(id=id)
    #         except Comments.DoesNotExist:
    #             return Response({"error":"Comment not found"}, status=status.HTTP_404_NOT_FOUND)
    #         data = self.serializer_class(
    #             comment
    #         ).data
    #         return Response({"data":data}, status=status.HTTP_200_OK)
    #     return Response({
    #         "data": self.serializer_class(comments, many=True).data
    #     }, status=status.HTTP_200_OK)

    def post(self, request, id, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                workout = Workout.objects.get(id=id)
            except Workout.DoesNotExist:
                return Response(
                    {"error": "Workout does not exist"}, status=status.HTTP_404_NOT_FOUND
                )
            serializer.save(user_id=request.user, workout_id=workout)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
