from models.workouts import WorkoutModel
from services import workouts

sample = WorkoutModel(
    id=1,
    name="workout1",
    user_id=1,
    scheduled_date="2026-11-11",
    completed_at="2026-11-11",
    total_duration=2,
)


def test_create():
    resp = workouts.create(sample)
    assert resp == sample


def test_get_exists():
    resp = workouts.get_one(1)
    assert resp == sample


def test_get_missing():
    resp = workouts.get_one(3)
    assert resp is None
