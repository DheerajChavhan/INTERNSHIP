from fastapi import APIRouter
from typing import Optional
from pydantic import BaseModel 

router=APIRouter(prefix="/order",tags=["Orders"])

@router.get("/{order_id}")
def discount(order_id:int,total:float,coupon:Optional[str]=None):

    if  coupon==None :
        return{
            "Order_id": order_id,
            "Total": total,
            "Discount_applied": "False",
            "Final_price": total
            }
    else: 
        discount_percent=10 
        final_price= total - 10*total/100 
        return{
            "Order_id": order_id, 
            "Total": total,
            "Discount_applied": "True",
            "Discount_percent": discount_percent,
            "Final_price": final_price
            } 
    
# Client Send this data
class OrderModel(BaseModel):
    order_id:int
    item_name:str
    quantity:int
    price_per_item:float

@router.post("/new")
def get_order(order:OrderModel):

# Server send this data
    total=order.quantity*order.price_per_item
    return {
        "message":"Order Created",
        "Order_Summary":{
            "Order_id":order.order_id,
            "item":order    .item_name,
            "Total_Amount":total
        }
    }   
    