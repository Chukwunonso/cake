from .crud_cake import cake
from .crud_user import user

# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.cake import Cake
# from app.schemas.cake import CakeCreate, CakeUpdate

# cake = CRUDBase[Cake, CakeCreate, CakeUpdate](Cake)
