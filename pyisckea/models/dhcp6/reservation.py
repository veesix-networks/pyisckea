from typing import List, Optional

from pydantic import Field

from pyisckea.models.generic.reservation import Reservation


class Reservation6(Reservation):
    ip_addresses: Optional[List[str]] = Field(default_factory=list)
    prefixes: Optional[List[str]] = Field(default_factory=list)
