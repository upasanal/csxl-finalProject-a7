import pytest
from sqlalchemy import delete
from sqlalchemy.orm import Session

from typing import Sequence

from backend.entities.floorplan.floorplan_entity import FloorplanEntity
from backend.models.coworking.floorplan.floorplan import Floorplan
from backend.models.coworking.floorplan.floorplan_details import FloorplanDetails

from ..reset_table_id_seq import reset_table_id_seq
from ..room_data import the_xl

__authors__ = ["Kris Jordan"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"

floorplan_1 = FloorplanDetails(
    id=1,
    boundaries="0 0 150 170",
    room=the_xl.to_room(),
    circle_tables=[],
    rectangle_tables=[],
)

monitor_seats = [floorplan_1]
floorplans: Sequence[Floorplan] = (
    monitor_seats 
)


def insert_fake_data(session: Session):
    for floorplan in floorplans:
        entity = FloorplanEntity.from_model(floorplan)
        session.add(entity)
    reset_table_id_seq(
        session, FloorplanEntity, FloorplanEntity.id, len(floorplans) + 1
    )


@pytest.fixture(autouse=True)
def fake_data_fixture(session: Session):
    insert_fake_data(session)
    session.commit()


def delete_all(session: Session):
    session.execute(delete(FloorplanEntity))
