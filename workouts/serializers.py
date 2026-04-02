from rest_framework import serializers

from .models import Comments, Exercise, Workout


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ["id", "name", "category", "muscle_group"]


class WorkoutSerializer(serializers.ModelSerializer):
    # This field is used for WRITING (POST/PUT) by passing a list of IDs
    exercise_ids = serializers.PrimaryKeyRelatedField(
        queryset=Exercise.objects.all(),
        many=True,
        write_only=True,
        source="exercises",  # Maps this input directly to the 'exercises' field
    )

    # This field is used for READING (GET) to show full data
    exercises = ExerciseSerializer(many=True, read_only=True)

    class Meta:
        model = Workout
        fields = [
            "id",
            "name",
            "user",
            "exercises",
            "exercise_ids",
            "scheduled_date",
            "completed_at",
            "total_duration",
            "created_at",
        ]
        read_only_fields = ["user", "created_at"]

    def create(self, validated_data):
        # Many-to-many fields can't be set during .create() until the object is saved
        exercises_data = validated_data.pop("exercises", [])
        workout = Workout.objects.create(**validated_data)
        workout.exercises.set(exercises_data)
        return workout


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ["user_id", "workout_id", "comment"]

        read_only_fields = ["user_id", "workout_id"]
