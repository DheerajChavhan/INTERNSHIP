from fastapi import FastAPI
from typing import Optional

app=FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/books/{book_id}",tags=["Books"])
def get_book(book_id:int,title:str,author:str,price:float,available:Optional[bool]=True):

    if available:
        return {
            "book_id": book_id,
            "available": True,
            "book": {
                "Title": title,
                "Author": author,
                "Price": price
            },
            "message": "Book updated successfully!"
               } 
    else:
        return{
            "book_id": book_id,
            "available": False,
            "book": {
                "Title": title,
                "Author": author,
                "Price": price
            },
            "message": "Book updated successfully!"
        }

@app.get("/users/create",tags=["User_Profile"])
def get_user(name:str,age:int,email:str,send_welcome_email:Optional[bool]=True):
        
    if age<18:
        return{"error": "User must be at least 18 years old."}

    else:
        return{
            "user":{
                "name": name,
                "age": age,
                "email": email
            },
            "send_welcome_email": send_welcome_email,
            "message": "User created successfully!"
            }

@app.get("/orders/{order_id}",tags=["Orders"])
def get_order(order_id:int,item_name:str,quantity:int,price_per_item:float,express_delivery:Optional[bool]=False):
    total = quantity * price_per_item 
    return{
        "order_id": order_id,
        "Express_delivery": express_delivery,
        "Total_amount": total,
        "Order": {
            "item_name": item_name,
            "quantity": quantity,
            "price_per_item": price_per_item
        },
        "message": "Order placed successfully!"
        }