from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from db.database import SessionLocal
from models import MenuItem
from schema import MenuItemCreate, MenuItemUpdate, MenuItemResponse

router = APIRouter(prefix="/menu")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#POST(Create Menu Item)
@router.post("/", response_model=MenuItemResponse,tags=["Create Menu"])
def create_menu_item(item: MenuItemCreate, db: Session = Depends(get_db)):
    db_item = MenuItem(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# GET(Get All Menu Item)
@router.get("/", response_model=List[MenuItemResponse],tags=["All Menu Items"])
def get_all_menu_items(db: Session = Depends(get_db)):
    return db.query(MenuItem).all()

# GET(Get Single Menu Item)
@router.get("/{id}", response_model=MenuItemResponse,tags=["Single Menu Items"])
def get_menu_item(id: int, db: Session = Depends(get_db)):
    item = db.query(MenuItem).filter(MenuItem.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return item

# PUT(Full Update)
@router.put("/{id}", response_model=MenuItemResponse,tags=["Update Full Info"])
def update_menu_item(id: int, item: MenuItemCreate, db: Session = Depends(get_db)):
    db_item = db.query(MenuItem).filter(MenuItem.id == id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Menu item not found")

    for key, value in item.dict().items():
        setattr(db_item, key, value)

    db.commit()
    db.refresh(db_item)
    return db_item

# PATCH (Partial Update)
@router.patch("/{id}", response_model=MenuItemResponse,tags=["Update Partial Info "])
def partial_update_menu_item(
    id: int,
    item: MenuItemUpdate,
    db: Session = Depends(get_db)
):
    db_item = db.query(MenuItem).filter(MenuItem.id == id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Menu item not found")

    for key, value in item.dict(exclude_unset=True).items():
        setattr(db_item, key, value)

    db.commit()
    db.refresh(db_item)
    return db_item

# DELETE(Delete Menu Item)
@router.delete("/{id}",tags=["Delete Menu Item"])
def delete_menu_item(id: int, db: Session = Depends(get_db)):
    db_item = db.query(MenuItem).filter(MenuItem.id == id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Menu item not found")

    db.delete(db_item)
    db.commit()
    return {"message": "Menu item deleted successfully"}
