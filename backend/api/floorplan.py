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


__authors__ = ["Ellie Kim, Shreeya Kantamsetty, Upasana Lamsal"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"

api = APIRouter(prefix="/api/floorplan")
openapi_tags = {
    "name": "Floorplan",
}



@api.get("/{id}/r", response_model=list[Seat], tags=["Floorplan"])
def get_seats_by_floorplan(
    id: int,
    floorplan_service: FloorplanService = Depends(),
) -> list[Seat]:
    """Get seats by floorplan
    Parameters:
        id: a string representing a unique identifier for floorplam
        floorplan_service: a valid floorplanService
    """
    return floorplan_service.get_seats_by_id(id)


@api.get("/{id}/boundary", response_model=str, tags=["Floorplan"])
def get_boundary_by_floorplan(
    id: int,
    floorplan_service: FloorplanService = Depends(),
) -> str:
    """Get boundary by a floorplan
    Parameters:
        id: a string representing a unique identifier for floorplam
        floorplan_service: a valid floorplanService
    """
    return floorplan_service.get_boundary_by_id(id)


@api.get("/{id}/circle_tables", response_model=list[CircleTable], tags=["Floorplan"])
def get_circletables_by_floorplan(
    id: int,
    floorplan_service: FloorplanService = Depends(),
) -> list[CircleTable]:
    """Get circle tables by floorplan
    Parameters:
        id: a string representing a unique identifier for floorplam
        floorplan_service: a valid floorplanService
    """
    return floorplan_service.get_circletables_by_id(id)


@api.get(
    "/{id}/rectangle_tables", response_model=list[RectangleTable], tags=["Floorplan"]
)
def get_rectangletables_by_floorplan(
    id: int,
    floorplan_service: FloorplanService = Depends(),
) -> list[RectangleTable]:
    """Get rectangle tables by floorplan
    Parameters:
        id: a string representing a unique identifier for floorplam
        floorplan_service: a valid floorplanService
    """
    return floorplan_service.get_rectangletables_by_id(id)


