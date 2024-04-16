import pytest
from sqlalchemy import delete
from sqlalchemy.orm import Session

from typing import Sequence

from backend.entities.floorplan.rectangletable_entity import RectangleTableEntity
from backend.models.coworking.floorplan.rectangle_table_details import (
    RectangleTableDetails,
)

from ..reset_table_id_seq import reset_table_id_seq
from backend.test.services.coworking.floorplan_data import floorplan_1

__authors__ = ["Shreeya Kantamsetty, Ellie Kim"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"

rectangle_table_1 = RectangleTableDetails(
    id=1, x="0", y="0", width="8", height="40", fill="gray", floorplan=floorplan_1
)

rectangle_table_2 = RectangleTableDetails(
    id=2, x="40", y="0", width="8", height="60", fill="gray", floorplan=floorplan_1
)

rectangle_table_3 = RectangleTableDetails(
    id=3, x="48", y="0", width="8", height="60", fill="gray", floorplan=floorplan_1
)

rectangle_table_4 = RectangleTableDetails(
    id=4, x="85", y="0", width="8", height="60", fill="gray", floorplan=floorplan_1
)
rectangle_table_5 = RectangleTableDetails(
    id=5, x="93", y="0", width="8", height="60", fill="gray", floorplan=floorplan_1
)

rectangle_table_6 = RectangleTableDetails(
    id=6, x="142", y="0", width="8", height="80", fill="gray", floorplan=floorplan_1
)

rectangle_table_7 = RectangleTableDetails(
    id=7, x="100", y="90", width="25", height="60", fill="gray", floorplan=floorplan_1
)

rectangle_tables = [rectangle_table_1, rectangle_table_2, rectangle_table_3, rectangle_table_4, rectangle_table_5, rectangle_table_6, rectangle_table_7]
tables: Sequence[RectangleTableDetails] = rectangle_tables


def insert_fake_data(session: Session):
    for rectangle_table in tables:
        entity = RectangleTableEntity.from_model(rectangle_table)
        session.add(entity)
    reset_table_id_seq(
        session, RectangleTableEntity, RectangleTableEntity.id, len(rectangle_tables) + 1
    )


@pytest.fixture(autouse=True)
def fake_data_fixture(session: Session):
    insert_fake_data(session)
    session.commit()

