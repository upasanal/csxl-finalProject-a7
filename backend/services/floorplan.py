"""
The Organizations Service allows the API to manipulate organizations data in the database.
"""

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from backend.entities.floorplan.floorplan_entity import FloorplanEntity
from backend.models.coworking.floorplan.circle_table import CircleTable
from backend.models.coworking.floorplan.floorplan import Floorplan
from backend.models.coworking.floorplan.rectangle_table import RectangleTable

from backend.models.coworking.seat import Seat

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
    
    def get_seats_by_id(self, id: int) -> list[Seat]: 
        entity = self._session.get(FloorplanEntity, id)
        result = entity.room.seats
        return [seat.to_model() for seat in result]
    
    def get_boundary_by_id(self, id: int) -> str: 
        entity = self._session.get(FloorplanEntity, id)
        return entity.boundaries
    
    def get_circletables_by_id(self, id: int) -> list[CircleTable]: 
        entity = self._session.get(FloorplanEntity, id)
        result = entity.circle_tables
        return [table.to_model() for table in result]
    
    def get_rectangletables_by_id(self, id: int) -> list[RectangleTable]: 
        entity = self._session.get(FloorplanEntity, id)
        result = entity.rectangle_tables
        return [table.to_model() for table in result]

    def get_floorplan_by_id(self, id: int) -> Floorplan: 
        entity = self._session.get(FloorplanEntity, id)
        return entity.to_model()

    def all(self) -> list[Organization]:
        """
        Retrieves all organizations from the table

        Returns:
            list[Organization]: List of all `Organization`
        """
        # Select all entries in `Organization` table
        query = select(OrganizationEntity)
        entities = self._session.scalars(query).all()

        # Convert entries to a model and return
        return [entity.to_model() for entity in entities]

    def get_by_slug(self, slug: str) -> OrganizationDetails:
        """
        Get the organization from a slug
        If none retrieved, a debug description is displayed.

        Parameters:
            slug: a string representing a unique organization slug

        Returns:
            Organization: Object with corresponding slug

        Raises:
            ResourceNotFoundException if no organization is found with the corresponding slug
        """

        # Query the organization with matching slug
        organization = (
            self._session.query(OrganizationEntity)
            .filter(OrganizationEntity.slug == slug)
            .one_or_none()
        )

        # Check if result is null
        if organization is None:
            raise ResourceNotFoundException(
                f"No organization found with matching slug: {slug}"
            )

        return organization.to_details_model()
