from fastapi import FastAPI, Path
from typing import Annotated

from models.workouts import WorkoutBody, WorkoutSetBody
from models.users import LoginBody, SignUpBody

app = FastAPI()


# MODEL


# VALIDATE WORKOUT
# VALIDATE WORKOUT SET
def validate_workout():
    pass


@app.get("/healthy")
def server_health():
    return "Server is healthy"


# TODOS
# SIGN UP
@app.post("/api/auth/register/")
def signup(body: SignUpBody):
    # Auth
    return {"message": "Sign up successful", "user": body}


# LOGIN
@app.post("/api/auth/login")
def login(body: LoginBody):
    return {"message": "Login successful", "user": ""}


# VIEW ALL WORKOUTS
@app.get("/api/workouts/")
def workout(limit: int = 8, page: int = 1):
    return {"message": "Successful", "limit": limit, "page": page}


# VIEW ALL WORKOUT SETS
@app.get("/api/workouts/{id}/sets")
def workout_sets(
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
        "workout_sets": [],
    }


# VIEW A SINGLE WORKOUT
@app.get("/api/workouts/{id}")
def single_workout(id: Annotated[int, Path(title="Workout id", ge=1)]):
    return {"id": id}


# VIEW A SINGLE WORKOUT SET
@app.get("/api/workouts/{workout_id}/sets/{id}")
def single_workout_sets(
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
@app.post("/api/workouts/")
def add_workout(body: WorkoutBody):
    return {"message": "Successful", "workout": body}


# ADD WORKOUT SET
@app.post("/api/workouts/{workout_id}/sets/")
def add_workout_sets(
    workout_id: Annotated[int, Path(title="Workout id", ge=1)], body: WorkoutSetBody
):
    return {
        "message": "Successfully added workout set",
        "workout_id": workout_id,
        "id": id,
        "workout_set": body,
    }


# UPDATE WORKOUT
@app.put("/api/workouts/{id}/")
def update_workout(
    body: WorkoutBody, id: Annotated[int, Path(title="Workout id", ge=1)]
):
    return {"message": "Successful", "id": id, "workout": body}


@app.put("/api/workouts/{workout_id}/sets/{id}")
def update_workout_sets(
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
@app.delete("/api/workouts/{id}/")
def delete_workout(id: Annotated[int, Path(title="Workout id", ge=1)]):
    return {
        "message": "Successfully deleted workout",
        "id": id,
    }


@app.delete("/api/workouts/{workout_id}/sets/{id}")
def delete_workout_sets(
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
