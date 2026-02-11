from sqlalchemy import  create_engine
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker

DATABASE_URL="sqlite:///./blog_app.db"   #/// is used for relative path and ./ is for current directory

engine=create_engine(DATABASE_URL,connect_args={"check_same_thread":False}) 

#sessiomaker is creating a transaction and bind is to connect the database to session autocommit is permanent change and autoflush is temporary change
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db       #It will provide session one by one and maintain a connection with db
    finally:
        db.close()    #finally will close the session even when the transaction is failed or succeed 