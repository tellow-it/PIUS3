from fastapi import APIRouter, status, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi_utils.cbv import cbv
from schemas.base_schema import Response
from schemas.important import (ImportantSchema,
                               ShowImportant)
from db.session import get_db
from db.repository.important import ImportantCRUD
from fastapi_utils.inferring_router import InferringRouter

router = InferringRouter()


@cbv(router)
class ImportantController:
    db: Session = Depends(get_db)

    @router.get('/', status_code=status.HTTP_200_OK)
    async def get_all_important(self) -> Response:
        try:
            important_objs = ImportantCRUD.get_important(db=self.db)
            return Response(status_code=200, message=f'Success get importants', data=important_objs)
        except Exception as err:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))

    @router.get('/{important_id}', status_code=status.HTTP_200_OK)
    async def get_important_by_id(self, important_id: int) -> Response:
        important_obj = ImportantCRUD.get_important_by_id(important_id=important_id, db=self.db)
        if important_obj is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Important doesn't exist")
        return Response(status_code=200, message=f'Success get category: {important_id}', data=important_obj)

    @router.post("/create", status_code=status.HTTP_201_CREATED)
    async def create_new_important(self, important: ImportantSchema) -> Response:
        try:
            important_obj = ImportantCRUD.create_important(important=important, db=self.db)
            return Response(status_code=200, message=f'Success create important', data=important_obj)
        except Exception as err:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))

    @router.put('/update', status_code=status.HTTP_200_OK)
    async def update_important(self, important: ShowImportant) -> Response:
        try:
            important_obj = ImportantCRUD.update_important(important=important, db=self.db)
            return Response(status_code=200, message=f'Success update: {important.id}', data=important_obj)
        except Exception as err:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))

    @router.delete('/delete/{important_id}', status_code=status.HTTP_200_OK)
    async def delete_important_by_id(self, important_id: int) -> Response:
        try:
            ImportantCRUD.delete_important(important_id=important_id, db=self.db)
            return Response(status_code=200, message=f'Success delete important: {important_id}')
        except Exception as err:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))
