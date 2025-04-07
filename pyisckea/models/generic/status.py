from typing import List, Optional

from pydantic import Field

from pyisckea.models.generic import Sockets
from pyisckea.models.generic.base import KeaBaseModel
from pyisckea.models.generic.high_availability import HighAvailability


class StatusGet(KeaBaseModel):
    pid: int
    uptime: int
    reload: int
    multi_threading_enabled: Optional[bool] = None
    sockets: Optional[Sockets] = None
    high_availability: Optional[List[HighAvailability]] = Field(default_factory=list)
