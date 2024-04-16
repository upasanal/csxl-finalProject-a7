"""RectangleTableDetails extends information about a RectangleTable, including its Room, to the RectangleTable model."""

from pydantic import BaseModel

from backend.models.coworking.floorplan.circle_table import CircleTable
from backend.models.coworking.floorplan.circle_table_details import CircleTableDetails
from backend.models.coworking.floorplan.floorplan import Floorplan
from backend.models.coworking.floorplan.rectangle_table import RectangleTable
from backend.models.coworking.floorplan.rectangle_table_details import RectangleTableDetails


__authors__ = ["Shreeya Kantamsetty, Ellie Kim"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"


class FloorplanDetails(Floorplan, BaseModel):
    circle_tables: list[CircleTableDetails]
    rectangle_tables: list[RectangleTableDetails]
