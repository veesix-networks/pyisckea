from typing import List, Optional

from pydantic import Field

from pykeadhcp.models.dhcp6.pd_pool import PDPool
from pykeadhcp.models.dhcp6.reservation import Reservation6
from pykeadhcp.models.generic.subnet import Subnet


class Subnet6(Subnet):
    preferred_lifetime: Optional[int] = None
    min_preferred_lifetime: Optional[int] = None
    max_preferred_lifetime: Optional[int] = None
    pd_allocator: Optional[str] = None
    pd_pools: Optional[List[PDPool]] = Field(default_factory=list)
    interface_id: Optional[str] = None
    rapid_commit: Optional[bool] = None
    reservations: Optional[List[Reservation6]] = Field(default_factory=list)
