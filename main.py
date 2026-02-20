from fastapi import FastAPI, Query
from typing import Annotated
from pydantic import BaseModel
from enum import Enum

app = FastAPI()


# MODEL
class Roles(Enum):
    user = "user"
    admin = "admin"


class SignUpBody(BaseModel):
    first_name: Annotated[str, Query(max_length=20)]
    middle_name: Annotated[str | None, Query(max_length=20)]
    last_name: Annotated[str, Query(max_length=20)]
    password: Annotated[str, Query(max_length=16,min_length=8)]
    role: Annotated[str | Roles, Query(max_length=20)] = Roles.user
    username: Annotated[str, Query(max_length=20)]


class LoginBody(BaseModel):
    username: str
    password: str


class WorkoutBody(BaseModel):
    name: Annotated[
        str,
        Query(
            title="Workout Name",
            max_length=20
        )
    ]
    user_id: Annotated[
        int, 
        Query(
            max_length=20
        )
    ]
    scheduled_date: Annotated[
        str, 
        Query(
            max_length=20
        )
    ]
    completed_at: Annotated[
        str, 
        Query(
            max_length=20
        )
    ]
    total_duration: Annotated[
        int, 
        Query(
            max_length=20,
            default=0
        )
    ]


class WorkoutSetBody(BaseModel):
    user_id: Annotated[int, Query(max_length=20)]
    workout_id: Annotated[int, Query(max_length=20)]
    exercise_id: Annotated[int, Query(max_length=20)]
    reps: Annotated[int, Query(max_length=20)]
    weight_lifted: Annotated[int | float, Query(max_length=20)] = 0
    rpe: Annotated[int, Query(max_length=20)]
    set_order: Annotated[int, Query(max_length=20)] = 0


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
def login():
    return {"message": "Login successful", "user": ""}


# VIEW ALL WORKOUTS
@app.get("/api/workouts/")
def workout(limit: int = 8, page: int = 1):
    return {"message": "Successful", "limit": limit, "page": page}


# VIEW ALL WORKOUT SETS
@app.get("/api/workouts/{id}/sets")
def workout_sets(limit: int = 0, page: int = 0):
    return {"message": "Successful", "limit": limit, "page": page, "workout_sets": []}


# VIEW A SINGLE WORKOUT
@app.get("/api/workouts/{id}")
def single_workout(id: int):
    return {"id": id}


# VIEW A SINGLE WORKOUT SET
@app.get("/api/workouts/{workout_id}/sets/{id}")
def single_workout_sets(workout_id: int, id: int):
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
@app.post("/api/workouts/{workout_id}/sets/{id}")
def add_workout_sets(workout_id: int, id: int, body: WorkoutSetBody):
    return {
        "message": "Successfully added workout set",
        "workout_id": workout_id,
        "id": id,
        "workout_set": body,
    }


# UPDATE WORKOUT
@app.put("/api/workouts/{id}/")
def update_workout(body: WorkoutBody, id: int):
    return {"message": "Successful", "id": id, "workout": body}


@app.put("/api/workouts/{workout_id}/sets/{id}")
def update_workout_sets(workout_id: int, id: int, body: WorkoutSetBody):
    return {
        "message": "Successfully updated workout set",
        "workout_id": workout_id,
        "id": id,
        "workout_set": body,
    }


# DELETE WORKOUT
@app.delete("/api/workouts/{id}/")
def delete_workout(id: int):
    return {
        "message": "Successfully deleted workout",
        "id": id,
    }


@app.delete("/api/workouts/{workout_id}/sets/{id}")
def delete_workout_sets(workout_id: int, id: int):
    return {
        "message": "Successfully delete workout set",
        "workout_id": workout_id,
        "id": id,
    }
