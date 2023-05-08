from typing import List

from schemas.category import CategorySchema, ShowCategory
from db.models.categories import Category
from sqlalchemy.orm import Session


class CategoryCRUD:
    @classmethod
    def get_category_by_id(cls, category_id: int, db: Session) -> ShowCategory:
        return db.query(Category).filter(Category.id == category_id).first()

    @classmethod
    def get_category(cls, db: Session) -> List[ShowCategory]:
        category_object: List[ShowCategory] = db.query(Category).all()
        return category_object

    @classmethod
    def create_category(cls, category: CategorySchema, db: Session) -> ShowCategory:
        _category: ShowCategory = Category(name=category.name)
        db.add(_category)
        db.commit()
        db.refresh(_category)
        return _category

    @classmethod
    def update_category(cls, category: ShowCategory, db: Session) -> ShowCategory:
        _category: ShowCategory = CategoryCRUD.get_category_by_id(category_id=category.id, db=db)
        _category.name = category.name
        db.commit()
        db.refresh(_category)
        return _category

    @classmethod
    def delete_category(cls, category_id: int, db: Session):
        _category: ShowCategory = CategoryCRUD.get_category_by_id(category_id=category_id, db=db)
        db.delete(_category)
        db.commit()
