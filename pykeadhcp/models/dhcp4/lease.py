from typing import List, Optional
from pydantic import Field
from pykeadhcp.models.generic.lease import Lease, LeasePage


class Lease4(Lease):
    pass


class Lease4Page(LeasePage):
    count: int
    leases: Optional[List[Lease4]] = Field(default_factory=list)
