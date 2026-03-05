from pathlib import Path
from sqlite3 import connect, Connection, Cursor
from decouple import config

conn: Connection | None = None
curs: Cursor


def get_db(path: str | None = None, reset: bool = False):
    global conn, curs
    if conn:
        if not reset:
            return
        conn = None

    if path is None:
        BASE_DIR = Path(__file__).resolve().parents[1]
        db_dir = BASE_DIR / "db"
        path = config("WORKOUT_SQLITE_DB", cast=str, default=f"{db_dir}/workout.db")  # type: ignore

    conn = connect(path, check_same_thread=False)  # type: ignore
    curs = conn.cursor()


get_db()
