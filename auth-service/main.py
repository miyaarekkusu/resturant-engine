from fastapi import FastAPI

app = FastAPI(title="Restaurant Engine - Auth Service")

@app.get("/")
def read_root():
    return {"message": "認証サービスへようこそ"}

@app.post("/login")
def login(username: str):
    return {"status": "success", "user": username, "token": "fake-jwt-token"}