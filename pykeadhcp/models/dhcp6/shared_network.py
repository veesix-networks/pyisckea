from typing import List, Optional

from pydantic import Field

from pykeadhcp.models.dhcp6.subnet import Subnet6
from pykeadhcp.models.generic.shared_network import SharedNetwork


class SharedNetwork6(SharedNetwork):
    subnet6: Optional[List[Subnet6]] = Field(default_factory=list)
    interface_id: Optional[str] = None
    min_preferred_lifetime: Optional[int] = None
    max_preferred_lifetime: Optional[int] = None
    rapid_commit: Optional[bool] = None
