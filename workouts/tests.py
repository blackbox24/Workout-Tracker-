from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Exercise, Workout


class WorkoutAPITests(APITestCase):
    def setUp(self):
        # 1. Create a user and authenticate
        self.user = User.objects.create_user(username="trainee", password="password123")
        self.client.force_authenticate(user=self.user)

        # 2. Create sample exercises to link to workouts
        self.ex1 = Exercise.objects.create(
            name="Push-up", category="Strength", muscle_group="Chest"
        )
        self.ex2 = Exercise.objects.create(name="Squat", category="Strength", muscle_group="Quads")

        self.url = reverse("create_workout_view")  # Ensure this matches your urls.py name

    def test_create_workout_success(self):
        """Test creating a workout with multiple exercises."""
        data = {
            "name": "Morning Routine",
            "exercise_ids": [self.ex1.pk, self.ex2.pk],
            "total_duration": 30,
        }

        response = self.client.post(self.url, data, format="json")

        # Verify response
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "Morning Routine")

        # Verify DB state
        workout = Workout.objects.get(id=response.data["id"])
        self.assertEqual(workout.user, self.user)  # Confirms perform_create logic
        self.assertEqual(workout.exercises.count(), 2)
        self.assertIn(self.ex1, workout.exercises.all())

    def test_create_workout_unauthenticated(self):
        """Test that unauthenticated users cannot create workouts."""
        self.client.force_authenticate(user=None)
        response = self.client.post(self.url, {"name": "Unauthorized"}, format="json")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
