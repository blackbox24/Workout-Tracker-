from pydantic import BaseModel
from fastapi import Query
from typing import Annotated


class WorkoutBody(BaseModel):
    name: Annotated[str, Query(title="Workout Name", max_length=20)]
    user_id: Annotated[int, Query(max_length=20)]
    scheduled_date: Annotated[str, Query(max_length=20)]
    completed_at: Annotated[str, Query(max_length=20)]
    total_duration: Annotated[int, Query(max_length=20)]


class WorkoutSetBody(BaseModel):
    user_id: Annotated[int, Query(max_length=20)]
    workout_id: Annotated[int, Query(max_length=20)]
    exercise_id: Annotated[int, Query(max_length=20)]
    reps: Annotated[int, Query(max_length=20)]
    weight_lifted: Annotated[int | float, Query(max_length=20)] = 0
    rpe: Annotated[int, Query(max_length=20)]
    set_order: Annotated[int, Query(max_length=20)] = 0
