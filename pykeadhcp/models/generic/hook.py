from typing import Optional
from pykeadhcp.models.generic.base import KeaBaseModel


class Hook(KeaBaseModel):
    library: str
    parameters: Optional[dict] = None
    name: Optional[str] = None
