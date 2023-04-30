from db.base_class import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime


class Category(Base):
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, index=True)
    name = Column(String, unique=True, nullable=False)
    tasks = relationship('Task', back_populates='categories')
