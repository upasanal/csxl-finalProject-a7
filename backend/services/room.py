"""
The Room Service allows the API to manipulate rooms data in the database.
"""

from typing import Optional
from typing import Optional
from fastapi import Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from backend.entities.coworking.seat_entity import SeatEntity
from backend.entities.coworking.seat_entity import SeatEntity
from backend.entities.floorplan.floorplan_entity import FloorplanEntity
from backend.models.coworking.floorplan.circle_table import CircleTable

from backend.models.coworking.floorplan.circle_table_details import CircleTableDetails
from backend.models.coworking.floorplan.floorplan import Floorplan
from backend.models.coworking.floorplan.floorplan_details import FloorplanDetails
from backend.models.coworking.floorplan.rectangle_table import RectangleTable
from backend.models.coworking.floorplan.rectangle_table_details import (
    RectangleTableDetails,
)
from backend.models.coworking.seat_details import SeatDetails


from ..database import db_session
from ..models import Room
from ..models import RoomDetails
from ..models.user import User
from ..entities import RoomEntity
from .permission import PermissionService

from ..services.exceptions import ResourceNotFoundException
from datetime import datetime

__authors__ = ["Ajay Gandecha"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"


class RoomService:
    """Service that performs all of the actions on the `Room` table"""

    def __init__(
        self,
        session: Session = Depends(db_session),
        permission_svc: PermissionService = Depends(),
    ):
        """Initializes the database session."""
        self._session = session
        self._permission_svc = permission_svc

    def all(self) -> list[RoomDetails]:
        """Retrieves all rooms from the table

        Returns:
            list[RoomDetails]: List of all `RoomDetails`
        """
        # Select all entries in `Room` table
        query = select(RoomEntity).order_by(RoomEntity.capacity)
        entities = self._session.scalars(query).all()

        # Convert entries to a model and return
        return [entity.to_details_model() for entity in entities]

    def get_by_id(self, id: str) -> RoomDetails:
        """Gets the room from the table for an id.

        Args:
            id: ID of the room to retrieve.
        Returns:
            RoomDetails: Room based on the id.
        """
        # Select all entries in the `Room` table and sort by end date
        query = select(RoomEntity).filter(RoomEntity.id == id)
        entity = self._session.scalars(query).one_or_none()

        # Raise an error if no entity was found.
        if entity is None:
            raise ResourceNotFoundException(f"Room with id: {id} does not exist.")

        # Return the model
        return entity.to_details_model()

    """Based on a given room by id, it obtains the floorplan of the room."""

    def get_seats_by_id(self, id: str) -> Optional[list[SeatDetails]]:
        room_entity = self._session.query(RoomEntity).filter_by(id=id).first()
        if room_entity is None:
            raise ResourceNotFoundException(f"Room with id: {id} does not exist.")
        seats = [seat_entity.to_model() for seat_entity in room_entity.seats]
        return seats


    def get_seat_by_ids(self, room_id: str, seat_id: int) -> Optional[SeatDetails]:

        room_entity = self._session.query(RoomEntity).filter_by(id=room_id).first()
        if room_entity is None:
            raise ResourceNotFoundException(f"Room with id: {room_id} does not exist.")
        seat_entity = next(
            (seat for seat in room_entity.seats if seat.id == seat_id), None
        )
        if seat_entity is None:
            raise ResourceNotFoundException(
                f"Seat with id: {seat_id} in room {room_id} does not exist."
            )
        return seat_entity.to_model()


    def update_seat_by_ids(
        self, room_id: str, seat_id: int, x: int, y: int, subject: User
    ) -> Optional[SeatDetails]:
        """
        Updates a seat within a specific room.

        Args:
            subject: a valid User model representing the currently logged in User
            room_id: the ID of the room to which the seat belongs
            seat_id: the ID of the seat to update
            seat: seartdetails to update the seat with

        Returns:
            SeatDetails: Object updated in the table

        Raises:
            ResourceNotFoundException: If the room or seat does not exist
        """
        self._permission_svc.enforce(subject, "manage_seats", "room/")

        room_entity = self._session.query(RoomEntity).filter_by(id=room_id).first()
        if room_entity is None:
            raise ResourceNotFoundException(f"Room with id: {room_id} does not exist.")
        seat_entity = next(
            (seat for seat in room_entity.seats if seat.id == seat_id), None
        )
        if seat_entity is None:
            raise ResourceNotFoundException(
                f"Seat with id: {seat_id} in room {room_id} does not exist."
            )
        seat_entity.x = x
        seat_entity.y = y
        # Commit changes
        self._session.commit()
        # Return edited object
        return seat_entity.to_model()

    def get_floorplan_by_room_id(self, id: str) -> Optional[FloorplanDetails]:
        """Get the floorplan with the given id of the room."""
        room_entity = self._session.query(RoomEntity).filter_by(id=id).first()
        if room_entity is None:
            raise ResourceNotFoundException(f"Room with id: {id} does not exist.")
        if room_entity.floorplan is not None:
            return room_entity.floorplan.to_model()

    def get_boundaries_by_room_id(self, id: str) -> Optional[str]:
        floorplan_model = self.get_floorplan_by_room_id(id)
        if floorplan_model is not None:
            return floorplan_model.boundaries
        else:
            return None

    def get_circletables_by_room_id(
        self, id: str
    ) -> Optional[list[CircleTableDetails]]:
        floorplan_model = self.get_floorplan_by_room_id(id)
        if floorplan_model is not None:
            return floorplan_model.circle_tables
        else:
            return None

    def get_rectangletables_by_room_id(
        self, id: str
    ) -> Optional[list[RectangleTableDetails]]:
        floorplan_model = self.get_floorplan_by_room_id(id)
        if floorplan_model is not None:
            return floorplan_model.rectangle_tables
        else:
            return None

    def create(self, subject: User, room: RoomDetails) -> RoomDetails:
        """Creates a new room.

        Args:
            subject: a valid User model representing the currently logged in User
            room: Room to add to table

        Returns:
            RoomDetails: Object added to table
        """

        # Check if user has admin permissions
        self._permission_svc.enforce(subject, "room.create", f"room/")

        # Create new object
        room_entity = RoomEntity.from_model(room)

        # Add new object to table and commit changes
        self._session.add(room_entity)
        self._session.commit()

        # Return added object
        return room_entity.to_details_model()

    def update(self, subject: User, room: RoomDetails) -> RoomDetails:
        """Updates a room.

        Args:
            subject: a valid User model representing the currently logged in User
            room: Room to update

        Returns:
            RoomDetails: Object updated in the table
        """

        # Check if user has admin permissions
        self._permission_svc.enforce(subject, "room.update", f"room/{room.id}")

        # Find the entity to update
        room_entity = self._session.get(RoomEntity, room.id)

        # Raise an error if no entity was found
        if room_entity is None:
            raise ResourceNotFoundException(f"Room with id: {room.id} does not exist.")

        # Update the entity
        room_entity.nickname = room.nickname
        room_entity.building = room.building
        room_entity.room = room.room
        room_entity.capacity = room.capacity
        room_entity.reservable = room.reservable

        # Commit changes
        self._session.commit()

        # Return edited object
        return room_entity.to_details_model()

    def delete(self, subject: User, id: str) -> None:
        """Deletes a room.

        Args:
            subject: a valid User model representing the currently logged in User
            id: ID of room to delete
        """

        # Check if user has admin permissions
        self._permission_svc.enforce(subject, "room.delete", f"room/{id}")

        # Find the entity to delete
        room_entity = self._session.get(RoomEntity, id)

        # Raise an error if no entity was found
        if room_entity is None:
            raise ResourceNotFoundException(f"Room with id: {id} does not exist.")

        # Delete and commit changes
        self._session.delete(room_entity)
        self._session.commit()
