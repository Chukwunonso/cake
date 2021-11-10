from sqlalchemy.orm import Session

import crud
from schemas.cake import CakeCreate, CakeUpdate
from tests.utils.user import create_random_user
from tests.utils.cake import make_random_cake_data
from tests.utils.utils import random_lower_string


def test_create_cake(db: Session) -> None:
    data = make_random_cake_data()
    cake_in = CakeCreate(**data)
    cake = crud.cake.create(db=db, obj_in=cake_in)
    assert cake.name == data["name"]
    assert cake.comment == data["comment"]


def test_get_cake(db: Session) -> None:
    data = make_random_cake_data()
    cake_in = CakeCreate(**data)
    cake = crud.cake.create(db=db, obj_in=cake_in)
    stored_cake = crud.cake.get(db=db, id=cake.id)
    assert stored_cake
    assert cake.id == stored_cake.id
    assert cake.name == stored_cake.name
    assert cake.comment == stored_cake.comment


def test_update_cake(db: Session) -> None:
    data = make_random_cake_data()
    cake_in = CakeCreate(**data)
    cake = crud.cake.create(db=db, obj_in=cake_in)
    comment2 = random_lower_string()
    cake_update = CakeUpdate(comment=comment2)
    cake2 = crud.cake.update(db=db, db_obj=cake, obj_in=cake_update)
    assert cake.id == cake2.id
    assert cake.name == cake2.name
    assert cake2.comment == comment2


def test_delete_cake(db: Session) -> None:
    data = make_random_cake_data()
    cake_in = CakeCreate(**data)
    cake = crud.cake.create(db=db, obj_in=cake_in)
    cake2 = crud.cake.remove(db=db, id=cake.id)
    cake3 = crud.cake.get(db=db, id=cake.id)
    assert cake3 is None
    assert cake2.id == cake.id
    assert cake2.name == data["name"]
    assert cake2.comment == data["comment"]
