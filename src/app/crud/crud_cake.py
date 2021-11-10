from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.cake import Cake
from schemas.cake import CakeCreate, CakeUpdate


class CRUDCake(CRUDBase[Cake, CakeCreate, CakeUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: CakeCreate, owner_id: int
    ) -> Cake:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_owner(
        self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100
    ) -> List[Cake]:
        return (
            db.query(self.model)
            .filter(Cake.owner_id == owner_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


cake = CRUDCake(Cake)
