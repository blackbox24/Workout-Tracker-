from django.conf import settings
from django.db import models


class Exercise(models.Model):
    class Category(models.TextChoices):
        STRENGTH = "Strength", "Strength"
        CARDIO = "Cardio", "Cardio"
        FLEXIBILITY = "Flexibility", "Flexibility"
        BALANCE = "Balance", "Balance"
        HIIT = "HIIT", "HIIT"

    class MuscleGroup(models.TextChoices):
        CHEST = "Chest", "Chest"
        BACK = "Back", "Back"
        SHOULDERS = "Shoulders", "Shoulders"
        BICEPS = "Biceps", "Biceps"
        TRICEPS = "Triceps", "Triceps"
        FOREARMS = "Forearms", "Forearms"
        CORE = "Core", "Core"
        QUADS = "Quads", "Quads"
        HAMSTRINGS = "Hamstrings", "Hamstrings"
        GLUTES = "Glutes", "Glutes"
        CALVES = "Calves", "Calves"

    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=Category.choices, default=Category.STRENGTH)
    muscle_group = models.CharField(
        max_length=20, choices=MuscleGroup.choices, default=MuscleGroup.CHEST
    )

    def __str__(self) -> str:
        return self.name


class Workout(models.Model):
    # Django handles the ID field automatically as BigAutoField
    name = models.CharField(max_length=100)

    # Standard practice to reference the User model
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="workouts"
    )

    scheduled_date = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    exercises: models.ManyToManyField = models.ManyToManyField(
        "Exercise", related_name="workouts", blank=True
    )
    total_duration = models.IntegerField(default=0)  # Duration in minutes

    # auto_now_add handles the DEFAULT CURRENT_TIMESTAMP logic
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.user.username}"
