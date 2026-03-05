from fastapi import APIRouter, Path
from typing import Annotated
from models.workouts import WorkoutBody, WorkoutSetBody

router = APIRouter(prefix="/workouts", tags=["Workouts"])


@router.get("/api/workouts/")
async def workout(limit: int = 8, page: int = 1):
    data = workout
    return {"message": "Successful", "limit": limit, "page": page, "data": data}


# VIEW ALL WORKOUT SETS
@router.get("/api/workouts/{id}/sets")
async def workout_sets(
    id: Annotated[
        int,
        Path(
            title="Workout id",
            ge=1,
        ),
    ],
    limit: int = 0,
    page: int = 0,
):
    return {
        "message": "Successful",
        "id": id,
        "limit": limit,
        "page": page,
        "workout_sets": "",
    }


# VIEW A SINGLE WORKOUT
@router.get("/api/workouts/{id}")
async def single_workout(id: Annotated[int, Path(title="Workout id", ge=1)]):
    return {"id": id}


# VIEW A SINGLE WORKOUT SET
@router.get("/api/workouts/{workout_id}/sets/{id}")
async def single_workout_sets(
    workout_id: Annotated[int, Path(title="Workout id", ge=1)],
    id: Annotated[int, Path(title="Workout set id", ge=1)],
):
    return {
        "message": "Successful",
        "workout_id": workout_id,
        "id": id,
        "workout_sets": [],
    }


# ADD WORKOUT
@router.post("/api/workouts/")
async def add_workout(body: WorkoutBody):
    return {"message": "Successful", "workout": body}


# ADD WORKOUT SET
@router.post("/api/workouts/{workout_id}/sets/")
async def add_workout_sets(
    workout_id: Annotated[int, Path(title="Workout id", ge=1)], body: WorkoutSetBody
):
    return {
        "message": "Successfully added workout set",
        "workout_id": workout_id,
        "id": id,
        "workout_set": body,
    }


# UPDATE WORKOUT
@router.put("/api/workouts/{id}/")
async def update_workout(
    body: WorkoutBody, id: Annotated[int, Path(title="Workout id", ge=1)]
):
    return {"message": "Successful", "id": id, "workout": body}


@router.put("/api/workouts/{workout_id}/sets/{id}")
async def update_workout_sets(
    workout_id: Annotated[int, Path(title="Workout id", ge=1)],
    id: Annotated[int, Path(title="Workout set id", ge=1)],
    body: WorkoutSetBody,
):
    return {
        "message": "Successfully updated workout set",
        "workout_id": workout_id,
        "id": id,
        "workout_set": body,
    }


# DELETE WORKOUT
@router.delete("/api/workouts/{id}/")
async def delete_workout(id: Annotated[int, Path(title="Workout id", ge=1)]):
    return {
        "message": "Successfully deleted workout",
        "id": id,
    }


@router.delete("/api/workouts/{workout_id}/sets/{id}")
async def delete_workout_sets(
    workout_id: Annotated[int, Path(title="Workout id", ge=1)],
    id: Annotated[
        int,
        Path(
            title="Workout set id",
            ge=1,
        ),
    ],
):
    return {
        "message": "Successfully delete workout set",
        "workout_id": workout_id,
        "id": id,
    }
