from fastapi import APIRouter
from typing import Optional
from pydantic import BaseModel

router=APIRouter(prefix="/books",tags=["Books"])

class BookModel(BaseModel):
    title:str
    author:str
    price:int
    in_stock:Optional[bool]=True

@router.post("/new")
def get_book(book:BookModel):
    return{
        "Title": book.title,
        "Author": book.author,
        "Price": book.price,
        "In_Stock": book.in_stock
    }
