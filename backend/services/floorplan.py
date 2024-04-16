"""
The Organizations Service allows the API to manipulate organizations data in the database.
"""

from typing import Optional
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from backend.entities.floorplan.floorplan_entity import FloorplanEntity
from backend.models.coworking.floorplan.circle_table import CircleTable
from backend.models.coworking.floorplan.floorplan import Floorplan
from backend.models.coworking.floorplan.rectangle_table import RectangleTable

from backend.models.coworking.seat import Seat
from backend.models.coworking.seat_details import SeatDetails

from ..database import db_session
from ..models.organization import Organization
from ..models.organization_details import OrganizationDetails
from ..entities.organization_entity import OrganizationEntity
from ..models import User
from .permission import PermissionService

from .exceptions import ResourceNotFoundException


__authors__ = ["Ellie Kim", "Shreeya Kantamsetty"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"


class FloorplanService:
    """Service that performs all of the actions on the `Organization` table"""

    def __init__(
        self,
        session: Session = Depends(db_session),
        permission: PermissionService = Depends(),
    ):
        """Initializes the `OrganizationService` session, and `PermissionService`"""
        self._session = session
        self._permission = permission
