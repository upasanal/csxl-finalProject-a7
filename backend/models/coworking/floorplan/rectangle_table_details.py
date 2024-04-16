"""RectangleTableDetails extends information about a RectangleTable, including its Room, to the RectangleTable model."""

from pydantic import BaseModel

from backend.models.coworking.floorplan.floorplan import Floorplan
from backend.models.coworking.floorplan.rectangle_table import RectangleTable


__authors__ = ["Shreeya Kantamsetty, Ellie Kim"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"


class RectangleTableDetails(RectangleTable, BaseModel):
    floorplan: Floorplan | None = None
