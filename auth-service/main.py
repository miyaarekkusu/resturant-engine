from fastapi import FastAPI
from pydantic import BaseModel # データ構造を定義するためのライブラリ

app = FastAPI(title="Restaurant Engine - Auth Service")

# ユーザーが登録時送られてくるデータ型の定義
class UserRegistration(BaseModel):
    username: str
    password: str
    email: str

@app.get("/")
def home():
    return {"message": "Restaurant Engine 認証サービスが起動しました"}

@app.post("/register")
def register(user: UserRegistration):
    # ここで本来はデータベースに保存します (今はコンソールに出力するだけ)
    print(f"登録されたユーザー： {user.username}")
    return {"message": f"{user.username}の登録が完了しました"}