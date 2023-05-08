from fastapi import APIRouter, HTTPException
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from starlette import status

from schemas.category import (ShowCategory,
                              CategorySchema)
from schemas.base_schema import Response
from db.session import get_db
from db.repository.categories import CategoryCRUD

router = InferringRouter()


@cbv(router)
class Category:
    db: Session = Depends(get_db)

    @router.get('/', status_code=status.HTTP_200_OK)
    async def get_all_category(self) -> Response:
        try:
            category_objs = CategoryCRUD.get_category(db=self.db)
            return Response(status_code=200, message='Success get categories', data=category_objs)
        except Exception as err:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))

    @router.get('/{category_id}', status_code=status.HTTP_200_OK)
    async def get_category_by_id(self, category_id: int) -> Response:
        try:
            category_obj = CategoryCRUD.get_category_by_id(category_id=category_id, db=self.db)
            return Response(status_code=200, message=f'Success get category: {category_id}', data=category_obj)
        except Exception as err:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))

    @router.post("/create", status_code=status.HTTP_201_CREATED)
    async def create_category(self, category: CategorySchema) -> Response:
        try:
            category_obj = CategoryCRUD.create_category(category=category, db=self.db)
            return Response(status_code=200, message='Success create category', data=category_obj)
        except Exception as err:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))

    @router.put('/update', status_code=status.HTTP_200_OK)
    async def update_category(self, category: ShowCategory) -> Response:
        try:
            category_obj = CategoryCRUD.update_category(category=category, db=self.db)
            return Response(status_code=200, message=f'Success update: {category.id}', data=category_obj)
        except Exception as err:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))

    @router.delete('/delete/{category_id}', status_code=status.HTTP_200_OK)
    async def delete_category_by_id(self, category_id: int):
        try:
            CategoryCRUD.delete_category(category_id=category_id, db=self.db)
            return Response(status_code=200, message=f'Success delete category: {category_id}')
        except Exception as err:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))
