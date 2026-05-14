# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["MapView"]


class MapView(BaseModel):
    """
    The bounding box enclosing the geometric shape (area or line) that an individual result covers. place typed results have no mapView.
    """

    east: Optional[str] = None
    """Longitude of the eastern-side of the box."""

    north: Optional[str] = None
    """Longitude of the northern-side of the box."""

    south: Optional[str] = None
    """Longitude of the southern-side of the box."""

    west: Optional[str] = None
    """Longitude of the western-side of the box."""
