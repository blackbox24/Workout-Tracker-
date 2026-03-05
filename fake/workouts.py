from models.workouts import WorkoutModel
from typing import List

PREV_ID: int = 0
workouts = [
    WorkoutModel(
        id=0,
        name="workout1",
        user_id=1,
        scheduled_date="2026-11-11",
        completed_at=None,
        total_duration=2,
    )
]


def get_all() -> List[WorkoutModel]:
    return workouts


def get_single(id: int) -> WorkoutModel | None:
    for workout in workouts:
        if workout.id == id:
            return workout
    return None


def create(workout: WorkoutModel) -> WorkoutModel:
    global PREV_ID
    PREV_ID += 1
    workout.id = PREV_ID
    workouts.append(workout)
    return workout


def modify(workout: WorkoutModel, id: int) -> WorkoutModel | None:
    for i in range(0, len(workouts)):
        if workouts[i].id == id:
            workouts[i] = workout
            return workout
    return None


def replace(workout: WorkoutModel, id: int) -> WorkoutModel | None:
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
