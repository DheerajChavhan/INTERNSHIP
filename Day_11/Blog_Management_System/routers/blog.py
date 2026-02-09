from fastapi import APIRouter,Depends
from schema import BlogCreate,BlogDisplay
from db.database import get_db
from sqlalchemy.orm import Session
from models import dbBlog
from fastapi import HTTPException

router=APIRouter(
    prefix="/blogs",tags=["Blogs"]
)

# POST
@router.post("",response_model=BlogDisplay)
def create_blog(blog:BlogCreate,db:Session=Depends(get_db)):

    new_blog=dbBlog(
        title=blog.title,
        content=blog.content
        )

    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

# GET (All Blog)
@router.get("",response_model=list[BlogDisplay])    
def get_all_blogs(db:Session=Depends(get_db)):
    blogs=db.query(dbBlog).all()
    return blogs

# GET (Single Blog)
@router.get("/{id}",response_model=BlogDisplay)    
def get_blog(id:int,db:Session=Depends(get_db)):
    blog=db.query(dbBlog).filter(dbBlog.id==id).first()
    return blog

# PUT (Update)
@router.put("/{id}",response_model=BlogDisplay)    
def update_blog(id:int,blog:BlogCreate,db:Session=Depends(get_db)):
    ext_blog=db.query(dbBlog).filter(dbBlog.id==id).first()
    ext_blog.title=blog.title
    ext_blog.content=blog.content

    db.commit()
    db.refresh(ext_blog)
    return ext_blog

# DELETE
@router.delete("/{id}",status_code=200)   
def delete_blog(id:int,db:Session=Depends(get_db)):
    Blog=db.query(dbBlog).filter(dbBlog.id==id).first()
    
    if Blog is None:
        raise HTTPException(status_code=404,detail="Blog Not Found!!")
    
    db.delete(Blog)
    db.commit()

    return {"Blog Deleted Successfully!!"}