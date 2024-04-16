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
