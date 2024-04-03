"""Entity for Room."""

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.entities.floorplan.circletable_entity import CircleTableEntity
from backend.entities.floorplan.rectangletable_entity import RectangleTableEntity
from backend.entities.room_entity import RoomEntity
from ..entity_base import EntityBase
from typing import Self
from backend.models.coworking.floorplan.floorplan import Floorplan

__authors__ = ["Ellie Kim, Shreeya Kantamsetty"]
__copyright__ = "Copyright 2024"
__license__ = "MIT"

class FloorplanEntity(EntityBase):
    """Entity for floorplans for rooms under XL management."""

    __tablename__ = "floorplan"

    # Fields
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    boundaries: Mapped[str] = mapped_column(String)

    #RoomDetails Model Fields Follow

    # Establishes a one to one relationship between the floorplan and the room tables.
    room_id: Mapped[int] = mapped_column(ForeignKey("room.id"))

    # Relationship Field

    # Stores the room data of the floorplan, populated automatically by SQLAlchemy using the foriengn key column we defined above.
    room: Mapped["RoomEntity"] = relationship(back_populates = "room_for")

    # Stores the circular tables this floor plan has, populated automatically by SQLAlchemy using the foreign key column we defined above
    circle_tables: Mapped[list["CircleTableEntity"]] = relationship("CircleTableEntity", back_populates = "floorplan")

    rectangle_tables: Mapped[list["RectangleTableEntity"]] = relationship("RectangleTableEntity", back_populates = "floorplan")

    def to_model(self) -> Floorplan:
        return Floorplan(id = self.id, boundaries = self.boundaries)
    

    @classmethod
    def from_model(cls, model: Floorplan) -> Self:
        """Create an RoomEntity from a Room model.

        Args:
            model (Room): The model to create the entity from.

        Returns:
            Self: The entity (not yet persisted)."""
        return cls(
            id=model.id,
            boundaries=model.boundaries
        )
