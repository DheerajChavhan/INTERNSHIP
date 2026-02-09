from sqlalchemy import Column,Integer,String
from db.database import Base

class dbBlog(Base):
    __tablename__="Blogs"

    id=Column(Integer,primary_key=True,index=True)
    title=Column(String,nullable=False)
    content=Column(String)

class dbUser(Base):
    __tablename__="Users"

    id=Column(Integer,primary_key=True,index=True)
    username=Column(String,nullable=False,unique=True)
    email=Column(String,nullable=False)