from typing import Optional
from fastapi import APIRouter, Depends
from backend.models.coworking.floorplan.circle_table import CircleTable
from backend.models.coworking.floorplan.floorplan import Floorplan
from backend.models.coworking.floorplan.rectangle_table import RectangleTable

from backend.models.coworking.seat import Seat
from backend.services.floorplan import FloorplanService

from ..services import RoomService
from ..models import Room
from ..models import RoomDetails
from ..api.authentication import registered_user
from ..models.user import User


__authors__ = ["Ellie Kim, Shreeya Kantamsetty"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"

api = APIRouter(prefix="/api/floorplan")
openapi_tags = {
    "name": "Floorplan",
}

"""
    2. Get the seats given a floorplan (floorplan.py)
    3. get the tables given a floorplan (floorplan.py)
    4. get the boundaries given a floorplans (floorplan.py)
    5. put the seat coordinates for a seat given a seat biTCH (seat.py)
"""


@api.get("/{id}/r", response_model = list[Seat], tags = ["Floorplan"])
def get_seats_by_floorplan(id: int, floorplan_service: FloorplanService = Depends(), ) -> list[Seat]:
    return floorplan_service.get_seats_by_id(id)

@api.get("/{id}/boundary", response_model = str, tags = ["Floorplan"])
def get_boundary_by_floorplan(id: int, floorplan_service: FloorplanService = Depends(), ) -> str:
    return floorplan_service.get_boundary_by_id(id)

@api.get("/{id}/circle_tables", response_model = list[CircleTable], tags = ["Floorplan"])
def get_circletables_by_floorplan(id: int, floorplan_service: FloorplanService = Depends(), ) ->list[CircleTable]:
    return floorplan_service.get_circletables_by_id(id)


@api.get("/{id}/circle_tables", response_model = list[RectangleTable], tags = ["Floorplan"])
def get_rectangletables_by_floorplan(id: int, floorplan_service: FloorplanService = Depends(), ) -> list[RectangleTable]:
    return floorplan_service.get_rectangletables_by_id(id)



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
