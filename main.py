from fastapi import FastAPI
from routers import auth, workouts

app = FastAPI(title="Workout Backend")

app.include_router(auth.router)
app.include_router(workouts.router)


@app.get("/")
async def root():
    return {"message": "Time to workout!"}


@app.get("/health")
async def server_health():
    return {"status": "healthy"}
