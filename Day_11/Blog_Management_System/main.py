from fastapi import FastAPI
from db.database import engine,Base
from routers import blog

app=FastAPI(
    title="Blog Management System"
)

Base.metadata.create_all(bind=engine)
app.include_router(blog.router)

@app.get("/")
def root():
    return{
        "Message":"Application working Successfully"
    }
