from fastapi import FastAPI
from routers import orders,user,products

app=FastAPI()

@app.get("/")
def root():
    return "Hello Dheeraj"

@app.get("/Home")
def Home():
    return "Dheeraj is an Engineering Student"     

app.include_router(orders.router)
app.include_router(products.router)
app.include_router(user.router)