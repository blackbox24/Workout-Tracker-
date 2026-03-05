from models.workouts import WorkoutBody, WorkoutModel
from . import curs

curs.execute(
    """
        CREATE TABLE IF NOT EXISTS workouts(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100) NOT NULL,
            user_id INTEGER,
            scheduled_date TIMESTAMP NOT NULL,
            completed_at TIMESTAMP DEFAULT NULL,
            total_duration INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
    """
)


def row_to_model(row: tuple) -> WorkoutModel:
    id, name, user_id, scheduled_date, completed_at, total_duration, others = row
    return WorkoutModel(
        id=id,
        name=name,
        scheduled_date=scheduled_date,
        completed_at=completed_at,
        total_duration=total_duration,
        user_id=user_id,
    )


def model_to_dict(workout: WorkoutBody) -> dict:
    return workout.model_dump()


def get_one(id: int) -> WorkoutModel | None:
    stmt = "SELECT * FROM workouts WHERE id=:id"
    params = {"id": id}
    curs.execute(stmt, params)
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    return None


def get_all() -> list[WorkoutModel]:
    stmt = "SELECT * FROM workouts"
    curs.execute(stmt)
    rows = curs.fetchall()
    return [row_to_model(row) for row in rows]


def create(workout: WorkoutBody) -> WorkoutBody:
    stmt = """
        INSERT INTO workouts(name, user_id, scheduled_date, completed_at, total_duration) VALUES
        (:name, :user_id, :scheduled_date, :completed_at, :total_duration)    
    """
    params = model_to_dict(workout)
    curs.execute(stmt, params)
    return workout


def modify(workout: WorkoutBody, id: int) -> WorkoutBody:
    stmt = """
        UPDATE workouts SET
            name = :name,
            user_id = :user_id,
            scheduled_date = :scheduled_date,
            completed_at = :completed_at,
            total_duration = :total_duration
        WHERE id = :id 
    """
    params = model_to_dict(workout)
    params["id"] = id
    curs.execute(stmt, params)
    return workout


def delete(id: int):
    stmt = "DELETE FROM workouts WHERE id = :id"
    params = {"id": id}
    curs.execute(stmt, params)
