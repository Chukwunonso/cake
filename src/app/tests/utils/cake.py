import random
from typing import Optional

from sqlalchemy.orm import Session

import crud
import models
from schemas.cake import CakeCreate
from tests.utils.user import create_random_user
from tests.utils.utils import random_lower_string


def make_random_cake_data(**kwargs):

    random_props = dict(
        name=random_lower_string(),
        comment=random_lower_string(),
        image_url=f"https://{random_lower_string(8)}.com/image/2",
        yum_factor=random.randint(1, 5),
        id=random.randint(1, 200)
    )
    random_props.update(kwargs)
    return random_props


def create_random_cake(db: Session, *, owner_id: Optional[int] = None, **kwargs) -> models.Cake:
    """
    Create a random cake for testing. Random properties are created but can be overwritten to test bad data
    """
    if owner_id is None:
        user = create_random_user(db)
        owner_id = user.id
    random_props = make_random_cake_data(**kwargs)
    cake_in = CakeCreate(**random_props)
    return crud.cake.create_with_owner(db=db, obj_in=cake_in, owner_id=owner_id)
