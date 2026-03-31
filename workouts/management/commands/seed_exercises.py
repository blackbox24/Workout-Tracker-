from django.core.management.base import BaseCommand

from workouts.models import Exercise


class Command(BaseCommand):
    help = "Seeds the database with 20 initial exercises"

    def handle(self, *args, **kwargs):
        exercises_data = [
            ("Push-up", Exercise.Category.STRENGTH, Exercise.MuscleGroup.CHEST),
            ("Pull-up", Exercise.Category.STRENGTH, Exercise.MuscleGroup.BACK),
            ("Squat", Exercise.Category.STRENGTH, Exercise.MuscleGroup.QUADS),
            ("Deadlift", Exercise.Category.STRENGTH, Exercise.MuscleGroup.GLUTES),
            ("Plank", Exercise.Category.STRENGTH, Exercise.MuscleGroup.CORE),
            ("Running", Exercise.Category.CARDIO, Exercise.MuscleGroup.QUADS),
            ("Cycling", Exercise.Category.CARDIO, Exercise.MuscleGroup.QUADS),
            ("Burpees", Exercise.Category.HIIT, Exercise.MuscleGroup.CORE),
            ("Mountain Climbers", Exercise.Category.HIIT, Exercise.MuscleGroup.CORE),
            ("Bicep Curl", Exercise.Category.STRENGTH, Exercise.MuscleGroup.BICEPS),
            ("Tricep Dip", Exercise.Category.STRENGTH, Exercise.MuscleGroup.TRICEPS),
            ("Shoulder Press", Exercise.Category.STRENGTH, Exercise.MuscleGroup.SHOULDERS),
            ("Lunges", Exercise.Category.STRENGTH, Exercise.MuscleGroup.GLUTES),
            ("Leg Press", Exercise.Category.STRENGTH, Exercise.MuscleGroup.QUADS),
            ("Calf Raise", Exercise.Category.STRENGTH, Exercise.MuscleGroup.CALVES),
            ("Lat Pulldown", Exercise.Category.STRENGTH, Exercise.MuscleGroup.BACK),
            ("Hammer Curl", Exercise.Category.STRENGTH, Exercise.MuscleGroup.BICEPS),
            ("Yoga Stretch", Exercise.Category.FLEXIBILITY, Exercise.MuscleGroup.BACK),
            ("Single Leg Stand", Exercise.Category.BALANCE, Exercise.MuscleGroup.CALVES),
            ("Jumping Jacks", Exercise.Category.CARDIO, Exercise.MuscleGroup.CALVES),
        ]

        for name, cat, muscle in exercises_data:
            exercise, _ = Exercise.objects.get_or_create(
                name=name, category=cat, muscle_group=muscle
            )

        self.stdout.write(self.style.SUCCESS("Successfully seeded 20 exercises!"))
