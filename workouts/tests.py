from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Exercise, Workout


class WorkoutAPITests(APITestCase):
    def setUp(self):
        # 1. Create a user and authenticate
        self.user = User.objects.create_user(username="trainee", password="password123")
        self.user2 = User.objects.create_user(username="trainee2", password="password123")

        self.client.force_authenticate(user=self.user)

        # 2. Create sample exercises to link to workouts
        self.ex1 = Exercise.objects.create(
            name="Push-up", category="Strength", muscle_group="Chest"
        )
        self.ex2 = Exercise.objects.create(name="Squat", category="Strength", muscle_group="Quads")

        self.user_workout, _ = Workout.objects.get_or_create(
            defaults={"name": "Morning Routine", "total_duration": 30, "user": self.user2}
        )

        self.user_workout.exercises.add(self.ex1)

        self.create_workout_url = reverse(
            "list_create_workout_view"
        )  # Ensure this matches your urls.py name

    def test_create_workout_success(self):
        """Test creating a workout with multiple exercises."""
        data = {
            "name": "Morning Routine",
            "exercise_ids": [self.ex1.pk, self.ex2.pk],
            "total_duration": 30,
        }

        response = self.client.post(self.create_workout_url, data, format="json")

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
        response = self.client.post(
            self.create_workout_url, {"name": "Unauthorized"}, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_workout_success(self):
        url = reverse("list_create_workout_view")
        self.client.force_authenticate(user=self.user2)

        response = self.client.get(url)
        workouts = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(workouts) > 0)

    def test_retrieve_workout_success(self):
        url = reverse("retrieve_workout_view", args=[self.user_workout.pk])
        self.client.force_authenticate(user=self.user2)

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_workout_fail(self):
        url = reverse("retrieve_workout_view", args=[self.user_workout.pk])

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
