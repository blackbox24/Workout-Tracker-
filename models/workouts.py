from pydantic import BaseModel, Field


class WorkoutBody(BaseModel):
    name: str = Field(max_length=20)
    user_id: int
    scheduled_date: str = Field(max_length=200)
    completed_at: str = Field(max_length=200)
    total_duration: int


class WorkoutSetBody(BaseModel):
    user_id: int
    workout_id: int
    exercise_id: int
    reps: int
    weight_lifted: int | float = 0
    rpe: int
    set_order: int = 0


class ExerciseBody(BaseModel):
    name: str
    description: str | None = None
    category: str
    muscle_group: str
