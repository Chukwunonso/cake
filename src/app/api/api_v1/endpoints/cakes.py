from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Cake])
def read_cakes(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve cakes.
    """
    cakes = crud.cake.get_multi(db, skip=skip, limit=limit)
    return cakes


@router.post("/", response_model=schemas.Cake)
def create_cake(
    *,
    db: Session = Depends(deps.get_db),
    cake_in: schemas.CakeCreate,
) -> Any:
    """
    Create new cake.
    """
    cake = crud.cake.create(db=db, obj_in=cake_in)
    return cake


@router.put("/{id}", response_model=schemas.Cake)
def update_cake(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    cake_in: schemas.CakeUpdate,
) -> Any:
    """
    Update an cake.
    """
    cake = crud.cake.get(db=db, id=id)
    if not cake:
        raise HTTPException(status_code=404, detail="Cake not found")
    cake = crud.cake.update(db=db, db_obj=cake, obj_in=cake_in)
    return cake


@router.get("/{id}", response_model=schemas.Cake)
def read_cake(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Get cake by ID.
    """
    cake = crud.cake.get(db=db, id=id)
    if not cake:
        raise HTTPException(status_code=404, detail="Cake not found")
    return cake


@router.delete("/{id}", response_model=schemas.Cake)
def delete_cake(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Delete an cake.
    """
    cake = crud.cake.get(db=db, id=id)
    if not cake:
        raise HTTPException(status_code=404, detail="Cake not found")
    cake = crud.cake.remove(db=db, id=id)
    return cake
