from db.base_class import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime


class Important(Base):
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, index=True)
    level = Column(String, unique=True, nullable=False)
    tasks = relationship('Task', back_populates='important')
