from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth
from app.database import Base, engine


Base.metadata.create_all(bind=engine)
app = FastAPI(title="Workout Backend")

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, tags=["auth"])


@app.get("/")
async def root():
    return {"message": "Time to workout!"}


@app.get("/health")
async def server_health():
    return {"status": "healthy"}
