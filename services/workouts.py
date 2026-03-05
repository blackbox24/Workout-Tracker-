from data import workouts as data
from models.workouts import WorkoutModel, WorkoutBody


def get_all() -> list[WorkoutModel]:
    return data.get_all()


def get_one(id: int) -> WorkoutModel | None:
    return data.get_one(id)


def create(workout: WorkoutBody) -> WorkoutBody:
    return data.create(workout)


# def replace(workout: WorkoutModel, id: int) -> WorkoutModel | None:
#     return data.replace(workout, id)


def modify(workout: WorkoutBody, id: int) -> WorkoutBody | None:
    return data.modify(workout, id)


def delete(id: int) -> str | None:
    return data.delete(id)
