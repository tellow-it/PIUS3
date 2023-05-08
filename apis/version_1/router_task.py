from fastapi import APIRouter, HTTPException
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from starlette import status

from schemas.task import ShowTask, TaskSchema
from schemas.base_schema import Response
from db.session import get_db
from db.repository.tasks import TaskCRUD

router = InferringRouter()


@cbv(router)
class Task:
    db: Session = Depends(get_db)

    @router.get('/', status_code=status.HTTP_200_OK)
    async def get_all_task(self) -> Response:
        try:
            task_objs = TaskCRUD.get_task(db=self.db)
            return Response(status_code=200, message='Success get tasks', data=task_objs)
        except Exception as err:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))

    @router.get('/{task_id}', status_code=status.HTTP_200_OK)
    async def get_task_by_id(self, task_id: int) -> Response:
        try:
            task_obj = TaskCRUD.get_task_by_id(task_id=task_id, db=self.db)
            return Response(status_code=200, message=f'Success get category: {task_id}', data=task_obj)
        except Exception as err:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))

    @router.post("/create", status_code=status.HTTP_201_CREATED)
    async def create_task(self, task: TaskSchema) -> Response:
        try:
            task_obj = TaskCRUD.create_task(task=task, db=self.db)
            return Response(status_code=200, message='Success create category', data=task_obj)
        except Exception as err:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))

    @router.put('/update', status_code=status.HTTP_200_OK)
    async def update_task(self, task: ShowTask) -> Response:
        try:
            task_obj = TaskCRUD.update_task(task=task, db=self.db)
            return Response(status_code=200, message=f'Success update: {task.id}', data=task_obj)
        except Exception as err:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))

    @router.delete('/delete/{task_id}', status_code=status.HTTP_200_OK)
    async def delete_category_by_id(self, task_id: int):
        try:
            TaskCRUD.delete_task(task_id=task_id, db=self.db)
            return Response(status_code=200, message=f'Success delete category: {task_id}')
        except Exception as err:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))
