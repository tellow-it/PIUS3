from db.base_class import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime


class Task(Base):
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    date_create = Column(DateTime, default=datetime.now())
    status = Column(Boolean, default=False, nullable=False)
    deadline = Column(DateTime, nullable=True)
    category_id = Column(Integer, ForeignKey("category.id", ondelete='CASCADE'), nullable=False,
                         index=True
                         )
    important_id = Column(Integer, ForeignKey("important.id", ondelete='CASCADE'), nullable=False,
                          index=True)

    categories = relationship('Category', back_populates='tasks')
    important = relationship('Important', back_populates='tasks')
