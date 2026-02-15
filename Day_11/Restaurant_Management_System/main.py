from fastapi import FastAPI
from db.database import engine, Base
from routers import restaurant

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Restaurant Management System API")

app.include_router(restaurant.router)
