"""RoomDetails provides more information about a room in the coworking space.

Importantly, it includes a room's seats, if seats are reservable as in the XL collab.
"""

from typing import Optional
from backend.models.coworking.floorplan.floorplan import Floorplan
from .room import Room
from .coworking.seat import Seat

__authors__ = ["Upasana Lamsal"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"


class RoomDetails(Room):
    building: str
    room: str
    capacity: int
    reservable: bool
    seats: list[Seat] = []
    floorplan: Optional[Floorplan] = None

    def to_room(self) -> Room:
        """Converts the details model to a room model.

        Returns:
            Room: The model representation of the entity."""
        return Room(id=self.id, nickname=self.nickname)
