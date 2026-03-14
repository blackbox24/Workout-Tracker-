from sqlalchemy import (
    Column,
    BigInteger,
    String,
    Integer,
    DateTime,
    ForeignKey,
    Text,
    Enum,
    Numeric,
    CheckConstraint,
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    first_name = Column(String(255))
    middle_name = Column(String(255), nullable=True)
    last_name = Column(String(255))

    email = Column(String(255), unique=True, index=True)
    username = Column(String(255), unique=True, index=True)

    password = Column(String(255))
    role: Column[str] = Column(
        Enum("user", "admin", name="user_role"), server_default="user"
    )

    created_at = Column(DateTime, server_default=func.now())

    workouts = relationship(
        "Workout", back_populates="user", cascade="all, delete-orphan"
    )
    workout_sets = relationship("WorkoutSet", back_populates="user")


class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False, index=True)
    description = Column(Text(), nullable=False)
    category: Column[str] = Column(
        Enum("Strength", "Cardio", "Flexibility", "Plyometrics", name="category_types"),
        nullable=True,
    )
    muscle_group: Column[str] = Column(
        Enum(
            "Chest",
            "Back",
            "Legs",
            "Shoulders",
            "Arms",
            "Core",
            "Full Body",
            name="muscle_groups",
        ),
        nullable=True,
    )

    created_at = Column(DateTime, server_default=func.now())

    workout_sets = relationship("WorkoutSet", back_populates="exercise")

    # Relationships
    user = relationship("User", back_populates="workouts")
    sets = relationship(
        "WorkoutSet", back_populates="workout", cascade="all, delete-orphan"
    )


class Workout(Base):
    __tablename__ = "workouts"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    user_id = Column(BigInteger, ForeignKey("users.id"))

    scheduled_date = Column(DateTime)
    completed_at = Column(DateTime)

    total_duration = Column(Integer, default=0)

    created_at = Column(DateTime, server_default=func.now())

    user = relationship("User", back_populates="workouts")


class WorkoutSet(Base):
    __tablename__ = "workout_sets"

    id = Column(BigInteger, primary_key=True, autoincrement=True)

    user_id = Column(BigInteger, ForeignKey("users.id"))
    workout_id = Column(BigInteger, ForeignKey("workouts.id"))
    exercise_id = Column(BigInteger, ForeignKey("exercises.id"))

    reps = Column(Integer, nullable=False)
    rpe = Column(Integer)

    set_order = Column(Integer, server_default="0")

    weight_lifted = Column(Numeric(5, 2), server_default="0")

    created_at = Column(DateTime, server_default=func.now())

    __table_args__ = (CheckConstraint("rpe >= 0 AND rpe <= 10", name="chk_rpe_range"),)

    user = relationship("User", back_populates="workout_sets")
    workout = relationship("Workout", back_populates="sets")
    exercise = relationship("Exercise", back_populates="workout_sets")
