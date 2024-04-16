"""Entity for Room."""

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship, Session

from backend.entities.floorplan.circletable_entity import CircleTableEntity
from backend.entities.floorplan.rectangletable_entity import RectangleTableEntity
from backend.models.coworking.floorplan.circle_table import CircleTable
from backend.models.coworking.floorplan.floorplan_details import FloorplanDetails
from backend.models.coworking.floorplan.rectangle_table import RectangleTable
from ..entity_base import EntityBase
from typing import Self

__authors__ = ["Ellie Kim, Shreeya Kantamsetty"]
__copyright__ = "Copyright 2024"
__license__ = "MIT"


class FloorplanEntity(EntityBase):
    """Entity for floorplans for rooms under XL management."""

    __tablename__ = "floorplan"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    boundaries: Mapped[str] = mapped_column(String)
    room_id: Mapped[int] = mapped_column(String, ForeignKey("room.id"), nullable=True)

    # relationships
    room: Mapped["RoomEntity"] = relationship("RoomEntity", back_populates="floorplan")
    circle_tables: Mapped[list["CircleTableEntity"]] = relationship(
        "CircleTableEntity", back_populates="floorplan"
    )
    rectangle_tables: Mapped[list["RectangleTableEntity"]] = relationship(
        "RectangleTableEntity", back_populates="floorplan"
    )

    def to_model(self) -> FloorplanDetails:
        floorplan = FloorplanDetails(
            id=self.id,
            boundaries=self.boundaries,
            room=self.room.to_model() if self.room else None,
            circle_tables=[
                circle_table.to_model() for circle_table in self.circle_tables],
            rectangle_tables=[
                rectangle_table.to_model() for rectangle_table in self.rectangle_tables
            ],
        )
        return floorplan

    @classmethod
    def from_model(
        cls, model: FloorplanDetails, session: Session | None = None
    ) -> Self:
        """Create an RoomEntity from a Room model.

        Args:
            model (Room): The model to create the entity from.

        Returns:
            Self: The entity (not yet persisted)."""
        return cls(
            id=model.id,
            boundaries=model.boundaries,
            room_id=model.room.id if model.room else None,
        )
