from django.db.models import Count
from django.db.models.query import QuerySet
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Workout
from .permissions import IsWorkoutOwner
from .serializers import CommentSerializer, WorkoutScheduledDate, WorkoutSerializer


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


class UpdateScheduleWorkoutView(APIView):
    permission_classes = (
        IsAuthenticated,
        IsWorkoutOwner,
    )
    serializer_class = WorkoutScheduledDate

    def patch(self, request, id, *args, **kwargs):
        try:
            workout = Workout.objects.get(id=id)
        except Workout.DoesNotExist:
            return Response({"error": "Workout not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            scheduled_date = serializer.validated_data.get("scheduled_date")
            workout.scheduled_date = scheduled_date
            workout.save()
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenerateReportView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        if request.user is None:
            return Response(
                {"detail": "No Authentication providered"}, status=status.HTTP_401_UNAUTHORIZED
            )

        data = {"total_workouts": 0, "total_completed_workouts": 0, "total_workout_sets": 0}
        # filter users based on authenticated user
        workouts = Workout.objects.filter(user=request.user.pk)

        # Total number of workouts
        data["total_workouts"] = workouts.aggregate(count=Count("id"))["count"]
        # Total number of workouts where completed_at is not null
        data["total_completed_workouts"] = len(workouts.exclude(completed_at=None))

        # total number of workouts using distinct names
        data["total_workout_sets"] = workouts.aggregate(count=Count("name", distinct=True))["count"]

        return Response(data, status=status.HTTP_200_OK)
