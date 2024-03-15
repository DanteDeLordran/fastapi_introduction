from app.db.database import Base
from sqlalchemy import Column, Integer , String, Boolean, ForeignKey
from pydantic import BaseModel , Field

class User(Base):
    __tablename__ = 'users'
    
    _id = Column(Integer , primary_key=True , index=True)
    email = Column(String , unique=True)
    username = Column(String , unique=True)
    first_name = Column(String)
    last_name = Column(String)
    password = Column(String)
    is_active = Column(Boolean , default=True)
    role = Column(String)
    phone_number = Column(String)

class Todo(Base):
    __tablename__ = 'todos'
    
    _id = Column(Integer, primary_key=True , index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
    user_id = Column(Integer , ForeignKey('users._id'))
    
