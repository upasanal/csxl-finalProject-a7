"""Room data for tests."""

import pytest
from sqlalchemy.orm import Session

from backend.models.coworking.seat import Seat
from backend.models.coworking.seat_details import SeatDetails
from ...entities import RoomEntity
from ...models import RoomDetails
from .reset_table_id_seq import reset_table_id_seq

__authors__ = ["Kris Jordan"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"

the_xl = RoomDetails(
    id="SN156",
    building="Sitterson",
    room="156",
    nickname="The XL",
    capacity=40,
    reservable=False,
    seats=[
        Seat(
            id=1,
            title="Seat 1",
            shorthand="S1",
            reservable=True,
            has_monitor=True,
            sit_stand=True,
            x=9,
            y=10,
        ),
        Seat(
            id=2,
            title="Seat 2",
            shorthand="S2",
            reservable=True,
            has_monitor=True,
            sit_stand=True,
            x=9,
            y=30,
        ),
        Seat(
            id=3,
            title="Seat 3",
            shorthand="S3",
            reservable=True,
            has_monitor=True,
            sit_stand=False,
            x=40,
            y=10,
        ),
        Seat(
            id=4,
            title="Seat 4",
            shorthand="S4",
            reservable=True,
            has_monitor=True,
            sit_stand=False,
            x=40,
            y=30,
        ),
        Seat(
            id=5,
            title="Seat 5",
            shorthand="S5",
            reservable=True,
            has_monitor=True,
            sit_stand=False,
            x=40,
            y=50,
        ),
        Seat(
            id=6,
            title="Seat 6",
            shorthand="S6",
            reservable=True,
            has_monitor=True,
            sit_stand=False,
            x=56,
            y=10,
        ),
        Seat(
            id=7,
            title="Seat 7",
            shorthand="S7",
            reservable=True,
            has_monitor=True,
            sit_stand=False,
            x=56,
            y=30,
        ),
        Seat(
            id=8,
            title="Seat 8",
            shorthand="S8",
            reservable=True,
            has_monitor=True,
            sit_stand=False,
            x=56,
            y=50,
        ),
        Seat(
            id=9,
            title="Seat 9",
            shorthand="S9",
            reservable=True,
            has_monitor=True,
            sit_stand=False,
            x=85,
            y=10,
        ),
        Seat(
            id=10,
            title="Seat 10",
            shorthand="S10",
            reservable=True,
            has_monitor=True,
            sit_stand=False,
            x=85,
            y=30,
        ),
        Seat(
            id=11,
            title="Seat 11",
            shorthand="S11",
            reservable=True,
            has_monitor=True,
            sit_stand=False,
            x=85,
            y=50,
        ),
        Seat(
            id=12,
            title="Seat 12",
            shorthand="S12",
            reservable=True,
            has_monitor=True,
            sit_stand=False,
            x=101,
            y=10,
        ),
        Seat(
            id=13,
            title="Seat 13",
            shorthand="S13",
            reservable=True,
            has_monitor=True,
            sit_stand=False,
            x=101,
            y=30,
        ),
        Seat(
            id=14,
            title="Seat 14",
            shorthand="S14",
            reservable=True,
            has_monitor=True,
            sit_stand=False,
            x=101,
            y=50,
        ),
        Seat(
            id=15,
            title="Seat 15",
            shorthand="S15",
            reservable=True,
            has_monitor=True,
            sit_stand=True,
            x=142,
            y=10,
        ),
        Seat(
            id=16,
            title="Seat 16",
            shorthand="S16",
            reservable=True,
            has_monitor=True,
            sit_stand=True,
            x=142,
            y=30,
        ),
        Seat(
            id=17,
            title="Seat 17",
            shorthand="S17",
            reservable=True,
            has_monitor=True,
            sit_stand=True,
            x=142,
            y=50,
        ),
        Seat(
            id=18,
            title="Seat 18",
            shorthand="S18",
            reservable=True,
            has_monitor=True,
            sit_stand=True,
            x=142,
            y=70,
        ),
    ],
    floorplan=None,
)

group_a = RoomDetails(
    id="SN135",
    building="Sitterson",
    room="135",
    nickname="Group A",
    capacity=4,
    reservable=True,
    seats=[],
    floorplan=None,
)

group_b = RoomDetails(
    id="SN137",
    building="Sitterson",
    room="137",
    nickname="Group B",
    capacity=4,
    reservable=True,
    seats=[],
    floorplan=None,
)

group_c = RoomDetails(
    id="SN141",
    building="Sitterson",
    room="141",
    nickname="Group C",
    capacity=6,
    reservable=True,
    seats=[],
    floorplan=None,
)

pair_a = RoomDetails(
    id="SN139",
    building="Sitterson",
    room="139",
    nickname="Pair A",
    capacity=2,
    reservable=True,
    seats=[],
    floorplan=None,
)

new_room = RoomDetails(
    id="FB009",
    building="Fred Brooks",
    room="009",
    nickname="Large Room",
    capacity=100,
    reservable=False,
    seats=[],
    floorplan=None,
)

edited_xl = RoomDetails(
    id="SN156",
    building="Sitterson",
    room="156",
    nickname="The CSXL",
    capacity=100,
    reservable=False,
    seats=[],
    floorplan=None,
)

rooms = [the_xl, group_a, group_b, group_c, pair_a]


def insert_fake_data(session: Session):
    for room in rooms:
        entity = RoomEntity.from_model(room)
        session.add(entity)

    # Don't need to reset room sequence because its ID is a string


@pytest.fixture(autouse=True)
def fake_data_fixture(session: Session):
    insert_fake_data(session)
    session.commit()
