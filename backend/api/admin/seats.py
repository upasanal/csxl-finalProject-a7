from backend.models.coworking.seat_details import SeatDetails
from backend.models.room_details import RoomDetails

from fastapi import APIRouter, Depends, HTTPException

from backend.services.room import RoomService
from ...services import UserService, UserPermissionException
from ...models import User, Paginated, PaginationParams
from ..authentication import registered_user

from fastapi import Depends

api = APIRouter(prefix="/api/admin/seats")
openapi_tags = {
    "name": "(Admin) Seat",
    "description": "Seats are used to update seat coordinates and identifiers/fields.",
}


@api.put("", tags=["(Admin) Seat"])
def update_seat(
    seat: SeatDetails,
    room_id: str,
    seat_id: int,
    subject: User = Depends(registered_user),
    room_service: RoomService = Depends(),
) -> SeatDetails:
    """
    Update seat

    Parameters:
        seat: a valid seat model
        room_id: a valid room ID
        seat_id: a valid seat ID
        subject: a valid User model representing the currently logged in User
        room_service: a valid RoomService

    Returns:
        SeatDetails: Updated seat
    """
    return room_service.update_seat_by_ids(subject, room_id, seat_id, seat)
