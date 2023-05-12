from pydantic import BaseModel


class ImportantSchema(BaseModel):
    level: str

    class Config:
        orm_mode = True


class ShowImportant(ImportantSchema):
    id: int
