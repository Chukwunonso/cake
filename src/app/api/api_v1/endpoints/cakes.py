from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Cake])
def read_cakes(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve cakes.
    """
    if crud.user.is_superuser(current_user):
        cakes = crud.cake.get_multi(db, skip=skip, limit=limit)
    else:
        cakes = crud.cake.get_multi_by_owner(
            db=db, owner_id=current_user.id, skip=skip, limit=limit
        )
    return cakes


@router.post("/", response_model=schemas.Cake)
def create_cake(
    *,
    db: Session = Depends(deps.get_db),
    cake_in: schemas.CakeCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new cake.
    """
    cake = crud.cake.create_with_owner(db=db, obj_in=cake_in, owner_id=current_user.id)
    return cake


@router.put("/{id}", response_model=schemas.Cake)
def update_cake(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    cake_in: schemas.CakeUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an cake.
    """
    cake = crud.cake.get(db=db, id=id)
    if not cake:
        raise HTTPException(status_code=404, detail="Cake not found")
    if not crud.user.is_superuser(current_user) and (cake.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    cake = crud.cake.update(db=db, db_obj=cake, obj_in=cake_in)
    return cake


@router.get("/{id}", response_model=schemas.Cake)
def read_cake(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get cake by ID.
    """
    cake = crud.cake.get(db=db, id=id)
    if not cake:
        raise HTTPException(status_code=404, detail="Cake not found")
    if not crud.user.is_superuser(current_user) and (cake.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return cake


@router.delete("/{id}", response_model=schemas.Cake)
def delete_cake(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an cake.
    """
    cake = crud.cake.get(db=db, id=id)
    if not cake:
        raise HTTPException(status_code=404, detail="Cake not found")
    if not crud.user.is_superuser(current_user) and (cake.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    cake = crud.cake.remove(db=db, id=id)
    return cake
