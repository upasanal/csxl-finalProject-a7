import pytest
from sqlalchemy import delete
from sqlalchemy.orm import Session

from typing import Sequence

from backend.entities.floorplan.circletable_entity import CircleTableEntity
from backend.models.coworking.floorplan.circle_table import CircleTable
from backend.models.coworking.floorplan.circle_table_details import CircleTableDetails

from ..reset_table_id_seq import reset_table_id_seq
from backend.test.services.coworking.floorplan_data import floorplan_1

__authors__ = ["Shreeya Kantamsetty, Ellie Kim"]
__copyright__ = "Copyright 2024"
__license__ = "MIT"

circle_table_1 = CircleTableDetails(
    id=1, cx="25", cy="80", radius="10", fill="gray", floorplan=floorplan_1
)

circle_table_2 = CircleTableDetails(
    id=2, cx="60", cy="105", radius="10", fill="gray", floorplan=floorplan_1
)

circle_table_3 = CircleTableDetails(
    id=3, cx="25", cy="130", radius="10", fill="gray", floorplan=floorplan_1
)

circle_tables = [circle_table_1, circle_table_2, circle_table_3]
tables: Sequence[CircleTable] = circle_tables


def insert_fake_data(session: Session):
    for circle_table in tables:
        entity = CircleTableEntity.from_model(circle_table)
        session.add(entity)
    reset_table_id_seq(
        session, CircleTableEntity, CircleTableEntity.id, len(circle_tables) + 1
    )


@pytest.fixture(autouse=True)
def fake_data_fixture(session: Session):
    insert_fake_data(session)
    session.commit()

