"""Tests for Coworking Rooms Service."""

from unittest.mock import create_autospec
import pytest
from backend.models.coworking.floorplan.circle_table_details import CircleTableDetails
from backend.models.coworking.floorplan.floorplan_details import FloorplanDetails
from backend.models.coworking.floorplan.rectangle_table_details import RectangleTableDetails
from backend.models.coworking.seat_details import SeatDetails
from backend.services.exceptions import (
    ResourceNotFoundException,
    UserPermissionException,
)
from backend.services.permission import PermissionService
from ...services import RoomService
from ...models import RoomDetails

# Imported fixtures provide dependencies injected for the tests as parameters.
from .fixtures import room_svc

# Import the setup_teardown fixture explicitly to load entities in database
from .role_data import fake_data_fixture as fake_role_data_fixture
from .user_data import fake_data_fixture as fake_user_data_fixture
from .room_data import fake_data_fixture as fake_room_data_fixture

# Import the fake model data in a namespace for test assertions
from . import room_data
from . import user_data

__authors__ = ["Kris Jordan"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"


def test_list(room_svc: RoomService):
    rooms = room_svc.all()
    assert len(rooms) == len(room_data.rooms)
    assert isinstance(rooms[0], RoomDetails)


def test_list_ordered_by_capacity(room_svc: RoomService):
    rooms = room_svc.all()
    for i in range(1, len(rooms)):
        assert rooms[i - 1].capacity <= rooms[i].capacity


def test_get_by_id(room_svc: RoomService):
    room = room_svc.get_by_id(room_data.group_a.id)

    assert isinstance(room, RoomDetails)
    assert room.id == room_data.group_a.id


def test_get_by_id_not_found(room_svc: RoomService):
    with pytest.raises(ResourceNotFoundException):
        room = room_svc.get_by_id("500")
        pytest.fail() 
    
def test_get_seats_by_id(room_svc: RoomService): 
    seats = room_svc.get_seats_by_id(room_data.the_xl.id)
    if seats is not None: 
        if (len(seats) > 0):
            for seat in seats:
                assert isinstance(seat, SeatDetails)
                assert seat.room.id == room_data.the_xl.id
        else: 
            print(f"There were no seats for this id: {room_data.the_xl.id}")

def test_put_seats_by_id(room_svc: RoomService): 
    room = room_svc.get_by_id(room_data.the_xl.id)
    room_svc.update

def test_get_seats_by_id_invalid_room_id(room_svc: RoomService):
    invalid_room_id = "SN189"
    with pytest.raises(ResourceNotFoundException):
        room_svc.get_seats_by_id(invalid_room_id)

def test_get_boundaries_by_id(room_svc: RoomService):
    boundaries = room_svc.get_boundaries_by_room_id(room_data.the_xl.id)
    if boundaries is not None: 
        assert isinstance(boundaries, str)

def test_get_boundaries_by_invalid_room_id(room_svc: RoomService):
    invalid_room_id = "SN189"
    with pytest.raises(ResourceNotFoundException):
        room_svc.get_boundaries_by_room_id(invalid_room_id)
    
def test_get_floorplan_by_id(room_svc: RoomService): 
    floorplan = room_svc.get_floorplan_by_room_id(room_data.the_xl.id)
    if floorplan is not None: 
        assert isinstance(floorplan, FloorplanDetails)
        assert floorplan.room.id == room_data.the_xl.id

def test_get_floorplan_by_invalid_room_id(room_svc: RoomService):
    invalid_room_id = "SN189"
    with pytest.raises(ResourceNotFoundException):
        room_svc.get_floorplan_by_room_id(invalid_room_id)

def test_get_circletables_by_id(room_svc: RoomService): 
    circle_tables = room_svc.get_circletables_by_room_id(room_data.the_xl.id)
    if circle_tables is not None: 
        for circle_table in circle_tables: 
            assert isinstance(circle_table, CircleTableDetails)
            assert circle_table.floorplan.room.id == room_data.the_xl.id

def test_get_circletables_by_invalid_room_id(room_svc: RoomService):
    invalid_room_id = "SN189"
    with pytest.raises(ResourceNotFoundException):
        room_svc.get_circletables_by_room_id(invalid_room_id)

def test_get_rectangletables_by_id(room_svc: RoomService): 
    rectangle_tables = room_svc.get_rectangletables_by_room_id(room_data.the_xl.id)
    if rectangle_tables is not None: 
        for rectangle_table in rectangle_tables: 
            assert isinstance(rectangle_table, CircleTableDetails)
            assert rectangle_table.floorplan.room.id == room_data.the_xl.id

def test_get_rectangletables_by_invalid_room_id(room_svc: RoomService):
    invalid_room_id = "SN189"
    with pytest.raises(ResourceNotFoundException):
        room_svc.get_rectangletables_by_room_id(invalid_room_id)

def test_create_as_root(room_svc: RoomService):
    permission_svc = create_autospec(PermissionService)
    room_svc._permission_svc = permission_svc

    room = room_svc.create(user_data.root, room_data.new_room)

    permission_svc.enforce.assert_called_with(user_data.root, "room.create", "room/")
    assert isinstance(room, RoomDetails)
    assert room.id == room_data.new_room.id


def test_create_as_user(room_svc: RoomService):
    with pytest.raises(UserPermissionException):
        room = room_svc.create(user_data.user, room_data.new_room)
        pytest.fail()


def test_update_as_root(room_svc: RoomService):
    permission_svc = create_autospec(PermissionService)
    room_svc._permission_svc = permission_svc

    room = room_svc.update(user_data.root, room_data.edited_xl)

    permission_svc.enforce.assert_called_with(
        user_data.root, "room.update", f"room/{room.id}"
    )
    assert isinstance(room, RoomDetails)
    assert room.id == room_data.edited_xl.id


def test_update_as_root_not_found(room_svc: RoomService):
    permission_svc = create_autospec(PermissionService)
    room_svc._permission_svc = permission_svc

    with pytest.raises(ResourceNotFoundException):
        room = room_svc.update(user_data.root, room_data.new_room)
        pytest.fail()


def test_update_as_user(room_svc: RoomService):
    with pytest.raises(UserPermissionException):
        room = room_svc.create(user_data.user, room_data.edited_xl)
        pytest.fail()


def test_delete_as_root(room_svc: RoomService):
    permission_svc = create_autospec(PermissionService)
    room_svc._permission_svc = permission_svc

    room_svc.delete(user_data.root, room_data.group_b.id)

    permission_svc.enforce.assert_called_with(
        user_data.root, "room.delete", f"room/{room_data.group_b.id}"
    )

    rooms = room_svc.all()
    assert len(rooms) == len(room_data.rooms) - 1


def test_delete_as_root_not_found(room_svc: RoomService):
    permission_svc = create_autospec(PermissionService)
    room_svc._permission_svc = permission_svc

    with pytest.raises(ResourceNotFoundException):
        room = room_svc.delete(user_data.root, room_data.new_room.id)
        pytest.fail()


def test_delete_as_user(room_svc: RoomService):
    with pytest.raises(UserPermissionException):
        room = room_svc.delete(user_data.user, room_data.the_xl.id)
        pytest.fail()

