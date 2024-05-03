"""Seat data for tests."""

import pytest
from sqlalchemy import delete
from sqlalchemy.orm import Session
from ....entities.coworking import SeatEntity
from ....models.coworking.seat_details import SeatDetails
from ....models.coworking.seat import Seat
from typing import Sequence

from ..reset_table_id_seq import reset_table_id_seq
from ..room_data import the_xl, group_a

__authors__ = ["Kris Jordan"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"


monitor_seat_43 = SeatDetails(
    id=44,
    title="Communal Seat 44",
    shorthand="M42",
    reservable=True,
    has_monitor=False,
    sit_stand=False,
    x=10,
    y=162,
    room=the_xl.to_room(),
)


monitor_seat_42 = SeatDetails(
    id=43,
    title="Communal Seat 43",
    shorthand="M41",
    reservable=True,
    has_monitor=False,
    sit_stand=False,
    x=30,
    y=162,
    room=the_xl.to_room(),
)

monitor_seat_41 = SeatDetails(
    id=42,
    title="Communal Seat 42",
    shorthand="M40",
    reservable=True,
    has_monitor=False,
    sit_stand=False,
    x=50,
    y=162,
    room=the_xl.to_room(),
)

monitor_seat_40 = SeatDetails(
    id=41,
    title="Communal Seat 41",
    shorthand="M39",
    reservable=True,
    has_monitor=False,
    sit_stand=False,
    x=112,
    y=150,
    room=the_xl.to_room(),
)

monitor_seat_39 = SeatDetails(
    id=40,
    title="Communal Seat 40",
    shorthand="M38",
    reservable=True,
    has_monitor=False,
    sit_stand=False,
    x=125,
    y=144,
    room=the_xl.to_room(),
)

monitor_seat_38 = SeatDetails(
    id=39,
    title="Communal Seat 39",
    shorthand="M38",
    reservable=True,
    has_monitor=False,
    sit_stand=False,
    x=125,
    y=129,
    room=the_xl.to_room(),
)

monitor_seat_37 = SeatDetails(
    id=38,
    title="Communal Seat 38",
    shorthand="M37",
    reservable=True,
    has_monitor=False,
    sit_stand=False,
    x=125,
    y=114,
    room=the_xl.to_room(),
)

monitor_seat_36 = SeatDetails(
    id=37,
    title="Communal Seat 37",
    shorthand="M36",
    reservable=True,
    has_monitor=False,
    sit_stand=False,
    x=125,
    y=98,
    room=the_xl.to_room(),
)

monitor_seat_35 = SeatDetails(
    id=36,
    title="Communal Seat 36",
    shorthand="M35",
    reservable=True,
    has_monitor=False,
    sit_stand=False,
    x=125,
    y=98,
    room=the_xl.to_room(),
)

monitor_seat_34 = SeatDetails(
    id=35,
    title="Communal Seat 35",
    shorthand="M34",
    reservable=True,
    has_monitor=False,
    sit_stand=False,
    x=100,
    y=144,
    room=the_xl.to_room(),
)


monitor_seat_33 = SeatDetails(
    id=34,
    title="Communal Seat 34",
    shorthand="M33",
    reservable=True,
    has_monitor=False,
    sit_stand=False,
    x=100,
    y=129,
    room=the_xl.to_room(),
)

monitor_seat_32 = SeatDetails(
    id=33,
    title="Communal Seat 33",
    shorthand="M32",
    reservable=True,
    has_monitor=False,
    sit_stand=False,
    x=100,
    y=114,
    room=the_xl.to_room(),
)

monitor_seat_31 = SeatDetails(
    id=32,
    title="Communal Seat 32",
    shorthand="M31",
    reservable=True,
    has_monitor=False,
    sit_stand=False,
    x=100,
    y=98,
    room=the_xl.to_room(),
)


monitor_seat_30 = SeatDetails(
    id=31,
    title="Communal Seat 31",
    shorthand="M30",
    reservable=True,
    has_monitor=False,
    sit_stand=False,
    x=112,
    y=90,
    room=the_xl.to_room(),
)


monitor_seat_29 = SeatDetails(
    id=30,
    title="Communal Seat 30",
    shorthand="M29",
    reservable=True,
    has_monitor=False,
    sit_stand=False,
    x=25,
    y=140,
    room=the_xl.to_room(),
)

monitor_seat_28 = SeatDetails(
    id=29,
    title="Communal Seat 29",
    shorthand="M28",
    reservable=True,
    has_monitor=False,
    sit_stand=False,
    x=36,
    y=130,
    room=the_xl.to_room(),
)


monitor_seat_27 = SeatDetails(
    id=28,
    title="Communal Seat 28",
    shorthand="M27",
    reservable=True,
    has_monitor=False,
    sit_stand=False,
    x=25,
    y=120,
    room=the_xl.to_room(),
)


monitor_seat_26 = SeatDetails(
    id=27,
    title="Communal Seat 27",
    shorthand="M26",
    reservable=True,
    has_monitor=False,
    sit_stand=False,
    x=15,
    y=130,
    room=the_xl.to_room(),
)

monitor_seat_25 = SeatDetails(
    id=26,
    title="Communal Seat 26",
    shorthand="M25",
    reservable=True,
    has_monitor=False,
    sit_stand=False,
    x=60,
    y=115,
    room=the_xl.to_room(),
)

monitor_seat_24 = SeatDetails(
    id=25,
    title="Communal Seat 25",
    shorthand="M24",
    reservable=True,
    has_monitor=False,
    sit_stand=False,
    x=70,
    y=105,
    room=the_xl.to_room(),
)

monitor_seat_23 = SeatDetails(
    id=24,
    title="Communal Seat 24",
    shorthand="M23",
    reservable=True,
    has_monitor=False,
    sit_stand=False,
    x=60,
    y=95,
    room=the_xl.to_room(),
)


monitor_seat_22 = SeatDetails(
    id=23,
    title="Communal Seat 23",
    shorthand="M22",
    reservable=True,
    has_monitor=False,
    sit_stand=False,
    x=50,
    y=105,
    room=the_xl.to_room(),
)

monitor_seat_21 = SeatDetails(
    id=22,
    title="Communal Seat 22",
    shorthand="M21",
    reservable=True,
    has_monitor=False,
    sit_stand=False,
    x=25,
    y=90,
    room=the_xl.to_room(),
)

monitor_seat_20 = SeatDetails(
    id=21,
    title="Communal Seat 21",
    shorthand="M20",
    reservable=True,
    has_monitor=False,
    sit_stand=False,
    x=35,
    y=80,
    room=the_xl.to_room(),
)

monitor_seat_19 = SeatDetails(
    id=20,
    title="Communal Seat 20",
    shorthand="M19",
    reservable=True,
    has_monitor=False,
    sit_stand=False,
    x=25,
    y=70,
    room=the_xl.to_room(),
)

monitor_seat_18 = SeatDetails(
    id=19,
    title="Communal Seat 19",
    shorthand="M18",
    reservable=True,
    has_monitor=False,
    sit_stand=False,
    x=15,
    y=80,
    room=the_xl.to_room(),
)

monitor_seat_17 = SeatDetails(
    id=18,
    title="Standing Monitor 18",
    shorthand="M17",
    reservable=True,
    has_monitor=True,
    sit_stand=True,
    x=142,
    y=70,
    room=the_xl.to_room(),
)

monitor_seat_16 = SeatDetails(
    id=17,
    title="Standing Monitor 17",
    shorthand="M16",
    reservable=True,
    has_monitor=True,
    sit_stand=True,
    x=142,
    y=50,
    room=the_xl.to_room(),
)

monitor_seat_15 = SeatDetails(
    id=16,
    title="Standing Monitor 16",
    shorthand="M15",
    reservable=True,
    has_monitor=True,
    sit_stand=True,
    x=142,
    y=30,
    room=the_xl.to_room(),
)

monitor_seat_14 = SeatDetails(
    id=15,
    title="Standing Monitor 15",
    shorthand="M14",
    reservable=True,
    has_monitor=True,
    sit_stand=True,
    x=142,
    y=10,
    room=the_xl.to_room(),
)

monitor_seat_00 = SeatDetails(
    id=1,
    title="Standing Monitor 01",
    shorthand="M00",
    reservable=True,
    has_monitor=True,
    sit_stand=True,
    x=9,
    y=10,
    room=the_xl.to_room(),
)

monitor_seat_01: Seat = SeatDetails(
    id=2,
    title="Standing Monitor 02",
    shorthand="M01",
    reservable=True,
    has_monitor=True,
    sit_stand=True,
    x=9,
    y=30,
    room=the_xl.to_room(),
)

monitor_seat_02: Seat = SeatDetails(
    id=3,
    title="Standing Monitor 03",
    shorthand="M02",
    reservable=True,
    has_monitor=True,
    sit_stand=False,
    x=40,
    y=10,
    room=the_xl.to_room(),
)

monitor_seat_03: Seat = SeatDetails(
    id=4,
    title="Monitor 04",
    shorthand="M03",
    reservable=True,
    has_monitor=True,
    sit_stand=False,
    x=40,
    y=30,
    room=the_xl.to_room(),
)

monitor_seat_04: Seat = SeatDetails(
    id=5,
    title="Monitor 05",
    shorthand="M04",
    reservable=True,
    has_monitor=True,
    sit_stand=False,
    x=40,
    y=50,
    room=the_xl.to_room(),
)

monitor_seat_05: Seat = SeatDetails(
    id=6,
    title="Monitor 06",
    shorthand="M05",
    reservable=True,
    has_monitor=True,
    sit_stand=False,
    x=56,
    y=10,
    room=the_xl.to_room(),
)

monitor_seat_06: Seat = SeatDetails(
    id=7,
    title="Monitor 07",
    shorthand="M06",
    reservable=True,
    has_monitor=True,
    sit_stand=False,
    x=56,
    y=30,
    room=the_xl.to_room(),
)

monitor_seat_07: Seat = SeatDetails(
    id=8,
    title="Monitor 08",
    shorthand="M07",
    reservable=True,
    has_monitor=True,
    sit_stand=False,
    x=56,
    y=50,
    room=the_xl.to_room(),
)

monitor_seat_08: Seat = SeatDetails(
    id=9,
    title="Monitor 09",
    shorthand="M08",
    reservable=True,
    has_monitor=True,
    sit_stand=False,
    x=85,
    y=10,
    room=the_xl.to_room(),
)

monitor_seat_09: Seat = SeatDetails(
    id=10,
    title="Monitor 10",
    shorthand="M09",
    reservable=True,
    has_monitor=True,
    sit_stand=False,
    x=85,
    y=30,
    room=the_xl.to_room(),
)

monitor_seat_10 = SeatDetails(
    id=11,
    title="Monitor 11",
    shorthand="M10",
    reservable=True,
    has_monitor=True,
    sit_stand=False,
    x=85,
    y=50,
    room=the_xl.to_room(),
)
monitor_seat_11 = SeatDetails(
    id=12,
    title="Monitor 12",
    shorthand="M11",
    reservable=True,
    has_monitor=True,
    sit_stand=False,
    x=101,
    y=10,
    room=the_xl.to_room(),
)

monitor_seat_12 = SeatDetails(
    id=13,
    title="Monitor 13",
    shorthand="M12",
    reservable=True,
    has_monitor=True,
    sit_stand=False,
    x=101,
    y=30,
    room=the_xl.to_room(),
)

monitor_seat_13 = SeatDetails(
    id=14,
    title="Monitor 14",
    shorthand="M13",
    reservable=True,
    has_monitor=True,
    sit_stand=False,
    x=101,
    y=50,
    room=the_xl.to_room(),
)

monitor_seats = [
    monitor_seat_00,
    monitor_seat_01,
    monitor_seat_02,
    monitor_seat_03,
    monitor_seat_04,
    monitor_seat_05,
    monitor_seat_06,
    monitor_seat_07,
    monitor_seat_08,
    monitor_seat_09,
    monitor_seat_10,
    monitor_seat_11,
    monitor_seat_12,
    monitor_seat_13,
    monitor_seat_14,
    monitor_seat_15,
    monitor_seat_16,
    monitor_seat_17,
    monitor_seat_18,
    monitor_seat_19,
    monitor_seat_20,
    monitor_seat_21,
    monitor_seat_22,
    monitor_seat_23,
    monitor_seat_24,
    monitor_seat_25,
    monitor_seat_26,
    monitor_seat_27,
    monitor_seat_28,
    monitor_seat_29,
    monitor_seat_30,
    monitor_seat_31,
    monitor_seat_32,
    monitor_seat_33,
    monitor_seat_34,
    monitor_seat_35,
    monitor_seat_37,
    monitor_seat_38,
    monitor_seat_39,
    monitor_seat_40,
    monitor_seat_41,
    monitor_seat_42,
    monitor_seat_43,
]

# common_area_00 = SeatDetails(
#     id=20,
#     title="Common Area 00",
#     shorthand="C00",
#     reservable=False,
#     has_monitor=False,
#     sit_stand=False,
#     x=5,
#     y=0,
#     room=the_xl.to_room()
# )
# common_area_01 = SeatDetails(
#     id=21,
#     title="Common Area 01",
#     shorthand="C01",
#     reservable=False,
#     has_monitor=False,
#     sit_stand=False,
#     x=5,
#     y=1,
#     room=the_xl.to_room()
# )
# common_area_seats = [common_area_00, common_area_01]

# conference_table_00 = SeatDetails(
#     id=40,
#     title="Conference Table 01",
#     shorthand="G01",
#     reservable=True,
#     has_monitor=False,
#     sit_stand=False,
#     x=20,
#     y=20,
#     room=the_xl.to_room()
# )
# conference_table_01 = SeatDetails(
#     id=41,
#     title="Conference Table 02",
#     shorthand="G02",
#     reservable=False,
#     has_monitor=False,
#     sit_stand=False,
#     x=20,
#     y=21,
#     room=the_xl.to_room(),
# )
# conference_table_seats = [conference_table_00, conference_table_01]

seats: Sequence[Seat] = monitor_seats  # + common_area_seats + conference_table_seats

reservable_seats = [seat for seat in seats if seat.reservable]

unreservable_seats = [seat for seat in seats if not seat.reservable]


def insert_fake_data(session: Session):
    for seat in seats:
        entity = SeatEntity.from_model(seat)
        session.add(entity)
    reset_table_id_seq(session, SeatEntity, SeatEntity.id, len(seats) + 1)


@pytest.fixture(autouse=True)
def fake_data_fixture(session: Session):
    insert_fake_data(session)
    session.commit()


def delete_all(session: Session):
    session.execute(delete(SeatEntity))
