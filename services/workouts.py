from fake import workouts as data
from models.workouts import WorkoutBody


def get_all() -> list[WorkoutBody]:
    return data.get_all()


def get_one(id: int) -> WorkoutBody | None:
    return data.get_single(id)


def create(workout: WorkoutBody) -> WorkoutBody:
    return data.create(workout)


def replace(workout: WorkoutBody, id: int) -> WorkoutBody | None:
    return data.replace(workout, id)


def modify(workout: WorkoutBody, id: int) -> WorkoutBody | None:
    return data.modify(workout, id)


def delete(id: int) -> str | None:
    return data.delete(id)
