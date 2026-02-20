from fastapi import FastAPI

app = FastAPI()

# MODEL
# class SignUpModel():

@app.get("/healthy")
def server_health():
    return "Server is healthy"

# TODOS
# SIGN UP
@app.post("/api/auth/register/")
def signup():
    return {"message":"Sign up successful","user":""}

# LOGIN
@app.post("/api/auth/login")
def login():
    return {"message":"Login successful", "user":""}

# CREATE WORKOUT
# VIEW ALL WORKOUTS
# VIEW A SINGLE WORKOUT
@app.get("/api/workout/{id}")
def workout(id):
    return {"id": id}


# UPDATE WORKOUT
# DELETE WORKOUT