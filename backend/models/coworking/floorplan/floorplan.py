"""Seat models a physical working space in the coworking space."""

from pydantic import BaseModel

from backend.models.coworking.floorplan.circle_table import CircleTable
from backend.models.coworking.floorplan.rectangle_table import RectangleTable
from backend.models.coworking.seat import Seat
from backend.models.room import Room


class Floorplan(BaseModel):
    id: int
    boundaries: str



