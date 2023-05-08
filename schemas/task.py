from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class TaskSchema(BaseModel):
    name: str
    description: Optional[str]
    date_create: datetime
    status: bool
    deadline: Optional[datetime]
    category_id: int
    important_id: int


class ShowTask(TaskSchema):
    id: int

    class Config:
        orm_mode = True
