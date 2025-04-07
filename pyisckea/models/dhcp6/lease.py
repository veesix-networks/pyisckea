from typing import List, Optional

from pydantic import Field

from pyisckea.models.enums import Lease6TypeEnum
from pyisckea.models.generic.lease import Lease, LeasePage


class Lease6(Lease):
    duid: str
    iaid: int
    prefix_len: Optional[int] = None
    type: Optional[Lease6TypeEnum] = None


class Lease6Page(LeasePage):
    count: int
    leases: Optional[List[Lease6]] = Field(default_factory=list)
