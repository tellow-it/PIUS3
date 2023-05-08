from typing import List
from schemas.task import TaskSchema, ShowTask
from db.models.tasks import Task
from sqlalchemy.orm import Session


class TaskCRUD:
    @classmethod
    def get_task_by_id(cls, task_id: int, db: Session) -> ShowTask:
        return db.query(Task).filter(Task.id == task_id).first()

    @classmethod
    def get_task(cls, db: Session) -> List[ShowTask]:
        task_objects: List[ShowTask] = db.query(Task).all()
        return task_objects

    @classmethod
    def create_task(cls, task: TaskSchema, db: Session) -> ShowTask:
        _task: ShowTask = Task(name=task.name,
                               description=task.description,
                               date_create=task.date_create,
                               status=task.status,
                               deadline=task.deadline,
                               category_id=task.category_id,
                               important_id=task.important_id)
        db.add(_task)
        db.commit()
        db.refresh(_task)
        return _task

    @classmethod
    def update_task(cls, task: ShowTask, db: Session) -> ShowTask:
        _task: ShowTask = TaskCRUD.get_task_by_id(task_id=task.id, db=db)
        _task.name = task.name
        _task.description = task.description
        _task.status = task.status
        _task.deadline = task.deadline
        _task.category_id = task.category_id
        _task.important_id = task.important_id
        _task.date_create = task.date_create

        db.commit()
        db.refresh(_task)
        return _task

    @classmethod
    def delete_task(cls, task_id: int, db: Session):
        _task: ShowTask = TaskCRUD.get_task_by_id(task_id=task_id, db=db)
        db.delete(_task)
        db.commit()
