from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class Cake(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    comment = Column(String, index=True)
    image_url = Column(String, index=True)
    yum_factor = Column(Integer, index=True)
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="cakes")
