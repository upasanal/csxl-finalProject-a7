"""Entity for Room."""

from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.models.coworking.floorplan.circle_table_details import CircleTableDetails

from ..entity_base import EntityBase
from typing import Self, Optional
from backend.models.coworking.floorplan.circle_table import CircleTable

__authors__ = ["Ellie Kim, Shreeya Kantamsetty"]
__copyright__ = "Copyright 2024"
__license__ = "MIT"


class CircleTableEntity(EntityBase):
    """Entity for rectangular tables within floorplans under XL management."""

    __tablename__ = "circle"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    cx: Mapped[str] = mapped_column(String)
    cy: Mapped[str] = mapped_column(String)
    radius: Mapped[str] = mapped_column(String)
    fill: Mapped[str] = mapped_column(String)
    floorplan_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("floorplan.id"), nullable=True
    )

    # relationships
    floorplan: Mapped["FloorplanEntity"] = relationship(
        "FloorplanEntity", back_populates="circle_tables"
    )

    def to_model(self) -> CircleTableDetails:
        """Converts the entity to a model.

        Returns:
            Room: The model representation of the entity."""
        return CircleTableDetails(
            id=self.id,
            cx=self.cx,
            cy=self.cy,
            radius=self.radius,
            fill=self.fill,
        )

    @classmethod
    def from_model(cls, model: CircleTableDetails) -> Self:
        """Create an RoomEntity from a Room model.

        Args:
            model (Room): The model to create the entity from.

        Returns:
            Self: The entity (not yet persisted)."""
        return cls(
            id=model.id,
            cx=model.cx,
            cy=model.cy,
            radius=model.radius,
            fill=model.fill,
            floorplan_id=model.floorplan.id,
        )
