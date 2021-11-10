from typing import Optional

from pydantic import BaseModel, AnyHttpUrl
from pydantic.types import conint, constr


class CakeBase(BaseModel):
    """
    Shared properties
    """
    name: constr(min_length=3, max_length=30)
    comment: constr(max_length=200)
    image_url: AnyHttpUrl
    yum_factor: conint(ge=1, le=5)


class CakeCreate(CakeBase):
    """
    Properties to receive on cake creation
    """
    pass


class CakeUpdate(CakeBase):
    """
    Properties to receive on cake update
    """
    name: Optional[constr(max_length=30)] = None
    comment: Optional[constr(max_length=200)] = None
    image_url: Optional[AnyHttpUrl] = None
    yum_factor: Optional[conint(ge=1, le=5)] = None


class CakeInDBBase(CakeBase):
    """
    Properties shared by models stored in DB
    """
    id: int
    name: str

    class Config:
        orm_mode = True


class Cake(CakeInDBBase):
    """
    Properties to receive on cake update
    """
    name: str
    comment: str
    image_url: str
    yum_factor: int


class CakeInDB(Cake):
    """
    Properties properties stored in DB
    """
    pass
