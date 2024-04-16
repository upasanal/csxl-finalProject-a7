"""Room API

Room routes are used to create, retrieve, and update Rooms."""

from typing import Optional
from typing import Optional
from fastapi import APIRouter, Depends
from backend.models.coworking.floorplan.circle_table_details import CircleTableDetails
from backend.models.coworking.floorplan.floorplan import Floorplan
from backend.models.coworking.floorplan.floorplan_details import FloorplanDetails

from backend.models.coworking.floorplan.rectangle_table_details import (
    RectangleTableDetails,
)
from backend.models.coworking.seat import Seat
from backend.models.coworking.seat_details import SeatDetails
from backend.services.floorplan import FloorplanService

from ..services import RoomService
from ..models import Room
from ..models import RoomDetails
from ..api.authentication import registered_user
from ..models.user import User


__authors__ = ["Ajay Gandecha"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"

api = APIRouter(prefix="/api/room")
openapi_tags = {
    "name": "Rooms",
    "description": "Create, update, delete, and retrieve rooms.",
}

"""
    1. Get floorplan given a room (room.py)
    2. Get the seats given a floorplan (floorplan.py)
    3. get the tables given a floorplan (floorplan.py)
    4. get the boundaries given a floorplans (floorplan.py)
    5. put the seat coordinates for a seat given a seat (seat.py)
"""


@api.get("/{id}/seats", response_model=list[SeatDetails], tags=["Room"])
def get_seats_by_room(
    id: str,
    room_service: RoomService = Depends(),
) -> Optional[list[SeatDetails]]:
    """Get seats by room
    Parameters:
        id: a string representing a unique identifier for room
        room_service: a valid roomService
    """
    return room_service.get_seats_by_id(id)


@api.get("/{id}/floorplan", response_model=FloorplanDetails, tags=["Rooms"])
def get_floorplan(
    id: str,
    room_service: RoomService = Depends(),
) -> Optional[FloorplanDetails]:
    return room_service.get_floorplan_by_room_id(id)

@api.get("/{id}/boundaries", response_model=str, tags=["Rooms"])
def get_boundaries(
    id: str,
    room_service: RoomService = Depends(),
) -> str:
    return room_service.get_boundaries_by_room_id(id) 


@api.get("/{id}/circle_tables", response_model=list[CircleTableDetails], tags=["Rooms"])
def get_circletables(
    id: str,
    room_service: RoomService = Depends(),
) -> list[CircleTableDetails]:
    return room_service.get_circletables_by_room_id(id)


@api.get(
    "/{id}/rectangle_tables", response_model=list[RectangleTableDetails], tags=["Rooms"]
)
def get_rectangletables(
    id: str,
    room_service: RoomService = Depends(),
) -> list[RectangleTableDetails]:
    return room_service.get_rectangletables_by_room_id(id)


@api.get("", response_model=list[RoomDetails], tags=["Rooms"])
def get_rooms(
    room_service: RoomService = Depends(),
) -> list[RoomDetails]:
    """
    Get all room

    Parameters:
        room_service: a valid RoomService

    Returns:
        list[RoomDetails]: All rooms in the `Room` database table
    """
    return room_service.all()


@api.get(
    "/{id}",
    response_model=RoomDetails,
    tags=["Rooms"],
)
def get_room_by_id(id: str, room_service: RoomService = Depends()) -> RoomDetails:
    """
    Get room with matching id

    Parameters:
        id: a string representing a unique identifier for a room
        room_service: a valid RoomService

    Returns:
        RoomDetails: RoomDetails with matching slug
    """

    return room_service.get_by_id(id)


@api.post("", response_model=RoomDetails, tags=["Rooms"])
def new_room(
    room: RoomDetails,
    subject: User = Depends(registered_user),
    room_service: RoomService = Depends(),
) -> RoomDetails:
    """
    Create room

    Parameters:
        room: a valid room model
        subject: a valid User model representing the currently logged in User
        room_service: a valid RoomService

    Returns:
        RoomDetails: Created room
    """

    return room_service.create(subject, room)


@api.put(
    "",
    response_model=RoomDetails,
    tags=["Rooms"],
)
def update_room(
    room: RoomDetails,
    subject: User = Depends(registered_user),
    room_service: RoomService = Depends(),
) -> RoomDetails:
    """
    Update room

    Parameters:
        room: a valid Room model
        subject: a valid User model representing the currently logged in User
        room_service: a valid RoomService

    Returns:
        RoomDetails: Updated room
    """

    return room_service.update(subject, room)


@api.delete("/{id}", response_model=None, tags=["Rooms"])
def delete_room(
    id: str,
    subject: User = Depends(registered_user),
    room_service: RoomService = Depends(),
):
    """
    Delete room based on id

    Parameters:
        id: a string representing a unique identifier for an room
        subject: a valid User model representing the currently logged in User
        room_service: a valid RoomService
    """

    room_service.delete(subject, id)
