from typing import Optional, List
from pydantic import Field
from pykeadhcp.models.generic.base import KeaBaseModel
from pykeadhcp.models.generic import Sockets
from pykeadhcp.models.generic.high_availability import HighAvailability


class StatusGet(KeaBaseModel):
    pid: int
    uptime: int
    reload: int
    multi_threading_enabled: Optional[bool] = None
    sockets: Optional[Sockets] = None
    high_availability: Optional[List[HighAvailability]] = Field(default_factory=list)
