from fastapi import FastAPI

app = FastAPI(title="Workout Backend")


@app.get("/")
async def root():
    return {"message": "Time to workout!"}


@app.get("/health")
async def server_health():
    return {"status": "healthy"}
