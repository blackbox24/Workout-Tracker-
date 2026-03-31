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

    def __str__(self):
        return self.name
