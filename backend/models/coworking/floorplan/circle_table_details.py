"""CircleTableDetails extends information about a CircleTable, including its Room, to the CircleTable model."""

from pydantic import BaseModel

from backend.models.coworking.floorplan.circle_table import CircleTable
from backend.models.coworking.floorplan.floorplan import Floorplan


__authors__ = ["Shreeya Kantamsetty, Ellie Kim"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"


class CircleTableDetails(CircleTable, BaseModel):
    floorplan: Floorplan | None = None
