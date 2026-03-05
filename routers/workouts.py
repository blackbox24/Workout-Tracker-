from fastapi import APIRouter, Path
from typing import Annotated
from models.workouts import WorkoutBody, WorkoutSetBody
from data import workouts as workout_service

router = APIRouter(prefix="/workouts", tags=["Workouts"])


@router.get("/")
async def workout(limit: int = 8, page: int = 1):
    # data = workout
    # return {"message": "Successful", "limit": limit, "page": page, "data": data}
    return workout_service.get_all()


# VIEW ALL WORKOUT SETS
@router.get("/{id}/sets")
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
@router.get("/{id}")
async def single_workout(id: Annotated[int, Path(title="Workout id", ge=1)]):
    return workout_service.get_one(id)


# VIEW A SINGLE WORKOUT SET
@router.get("/{workout_id}/sets/{id}")
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
@router.post("/")
async def add_workout(body: WorkoutBody):
    return workout_service.create(body)


# ADD WORKOUT SET
@router.post("/{workout_id}/sets/")
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
@router.put("/{id}/")
async def update_workout(
    body: WorkoutBody, id: Annotated[int, Path(title="Workout id", ge=1)]
):
    return workout_service.modify(body, id)


@router.put("/{workout_id}/sets/{id}")
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
@router.delete("/{id}/")
async def delete_workout(id: Annotated[int, Path(title="Workout id", ge=1)]):
    return workout_service.delete(id)


@router.delete("/{workout_id}/sets/{id}")
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
