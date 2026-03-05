from models.workouts import WorkoutBody
from fastapi.exceptions import HTTPException
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


def get_single(id: int) -> WorkoutBody | HTTPException:
    for workout in workouts:
        if workout.id == id:
            return workout
    raise HTTPException(status_code=404, detail="Workout not found")


def create(workout: WorkoutBody) -> WorkoutBody:
    global PREV_ID
    PREV_ID += 1
    workout.id = PREV_ID
    workouts.append(workout)
    return workout


def modify(workout: WorkoutBody, id: int) -> WorkoutBody | HTTPException:
    for i in range(0, len(workouts)):
        if workouts[i].id == id:
            workouts[i] = workout
            return workout
    raise HTTPException(status_code=404, detail="Workout not found")


def replace(workout: WorkoutBody, id: int) -> WorkoutBody | HTTPException:
    for i in range(0, len(workouts)):
        if workouts[i].id == id:
            workout.id = id
            workouts[i] = workout
            return workout
    raise HTTPException(status_code=404, detail="Workout not found")


def delete(id: int) -> str | None:
    for _workout in workouts:
        if _workout.id == id:
            workouts.remove(workouts[id])
            return "Deleted"
    raise HTTPException(status_code=404, detail="Workout not found")
