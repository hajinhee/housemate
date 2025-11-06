from fastapi import FastAPI
from app.api.routers import api_router

app = FastAPI(
    title="하우스메이트",
    description="(House Mate)",
)

app.include_router(api_router)


@app.get("/")
def root():
    return {"message": "HouseMate API 동작 중!"}
