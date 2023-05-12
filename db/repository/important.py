from typing import List

from schemas.important import ImportantSchema, ShowImportant
from db.models.important import Important
from sqlalchemy.orm import Session


class ImportantCRUD:

    @classmethod
    def get_important_by_id(cls, important_id: int, db: Session) -> ShowImportant:
        return db.query(Important).filter(Important.id == important_id).first()

    @classmethod
    def get_important(cls, db: Session) -> List[ShowImportant]:
        important_object: List[ShowImportant] = db.query(Important).all()
        return important_object

    @classmethod
    def create_important(cls, important: ImportantSchema, db: Session) -> ShowImportant:
        _important: ShowImportant = Important(level=important.level)
        db.add(_important)
        db.commit()
        db.refresh(_important)
        return _important

    @classmethod
    def update_important(cls, important: ShowImportant, db: Session) -> ShowImportant:
        _important: ShowImportant = ImportantCRUD.get_important_by_id(important_id=important.id, db=db)
        _important.level = important.level
        db.commit()
        db.refresh(_important)
        return _important

    @classmethod
    def delete_important(cls, important_id: int, db: Session):
        _important: ShowImportant = ImportantCRUD.get_important_by_id(important_id=important_id, db=db)
        db.delete(_important)
        db.commit()
