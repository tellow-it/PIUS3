from typing import Optional, Generic, TypeVar
from pydantic.generics import GenericModel

T = TypeVar('T')


class Response(GenericModel, Generic[T]):
    status_code: str
    message: str
    data: Optional[T]
