from typing import List, Optional
from pykeadhcp.models.generic.subnet import Subnet
from pykeadhcp.models.dhcp6.pd_pool import PDPool
from pykeadhcp.models.dhcp6.reservation import Reservation6


class Subnet6(Subnet):
    preferred_lifetime: Optional[int] = None
    min_preferred_lifetime: Optional[int] = None
    max_preferred_lifetime: Optional[int] = None
    pd_pools: Optional[List[PDPool]] = []
    interface_id: Optional[str] = None
    rapid_commit: Optional[bool] = None
    reservations: Optional[List[Reservation6]] = []
