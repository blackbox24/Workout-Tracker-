from models.workouts import WorkoutBody
from typing import List

PREV_ID: int = 0
workouts = [
    WorkoutBody(
        id=0,
        name="workout1",
        user_id=1,
        scheduled_date="2026-11-11",
        completed_at=None,
        total_duration=2,
    )
]


def get_all() -> List[WorkoutBody]:
    return workouts


def get_single(id: int) -> WorkoutBody | None:
    for workout in workouts:
        if workout.id == id:
            return workout
    return None


def create(workout: WorkoutBody) -> WorkoutBody:
    global PREV_ID
    PREV_ID += 1
    workout.id = PREV_ID
    workouts.append(workout)
    return workout


def modify(workout: WorkoutBody, id: int) -> WorkoutBody | None:
    for i in range(0, len(workouts)):
        if workouts[i].id == id:
            workouts[i] = workout
            return workout
    return None


def replace(workout: WorkoutBody, id: int) -> WorkoutBody | None:
    for i in range(0, len(workouts)):
        if workouts[i].id == id:
            workout.id = id
            workouts[i] = workout
            return workout
    return None


def delete(id: int) -> str | None:
    for _workout in workouts:
        if _workout.id == id:
            workouts.remove(workouts[id])
            return "Deleted"
    return None
