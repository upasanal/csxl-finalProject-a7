"""Entity for Room."""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..entity_base import EntityBase
from typing import Self, Optional
from backend.models.coworking.floorplan.rectangle_table import RectangleTable

__authors__ = ["Ellie Kim, Shreeya Kantamsetty"]
__copyright__ = "Copyright 2024"
__license__ = "MIT"

class RectangleTableEntity(EntityBase):
    """Entity for rectangular tables within floorplans under XL management."""

    __tablename__ = "rectangle"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    x: Mapped[str] = mapped_column(Integer)
    y: Mapped[str] = mapped_column(String)
    width: Mapped[str] = mapped_column(String)
    height: Mapped[str] = mapped_column(String)
    fill: Mapped[str] = mapped_column(String)

    floorplan_id = Column(Integer, ForeignKey('floorplan.id'))
    floorplan = relationship("FloorplanEntity", back_populates="rectangle_tables")

    def to_model(self) -> RectangleTable:
        """Converts the entity to a model.

        Returns:
            Room: The model representation of the entity."""
        return RectangleTable(id = self.id, x = self.x, y = self.y, width = self.width, height = self.height, fill = self.fill)


    @classmethod
    def from_model(cls, model: RectangleTable) -> Self:
        """Create an RoomEntity from a Room model.

        Args:
            model (Room): The model to create the entity from.

        Returns:
            Self: The entity (not yet persisted)."""
        return cls(
            id=model.id,
            x=model.x,
            y=model.y,
            width=model.width,
            height=model.height,
            fill=model.fill,
        )
