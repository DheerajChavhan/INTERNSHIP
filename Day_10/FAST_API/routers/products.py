from fastapi import APIRouter
from typing import Optional
from pydantic import BaseModel
router=APIRouter(prefix="/products",tags=["Products"])

@router.get("/")
def get_products(
    category : Optional[str] = None,   #Query parameter are always optional
    page : int = 1
): 
    return f"Fetching Products in {category} on the Page {page}"

class ProductModel(BaseModel):
    product_id:int
    



@router.post("/{product_id}")
def create_product(product_id:int,product:ProductModel,confirmed:Optional[bool]:False):
    total=product.quantity*product.price
    return{
        "message":"Product added Successfully",
        "Product_id":product_id,
        "Confirmed":confirmed,
        "Product_Detail":{
            
        }
    }    