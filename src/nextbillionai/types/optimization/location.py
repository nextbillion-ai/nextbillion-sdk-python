# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["Location"]


class Location(BaseModel):
    """Location info."""

    lat: float
    """Latitude of location."""

    lon: float
    """Longitude of location."""
