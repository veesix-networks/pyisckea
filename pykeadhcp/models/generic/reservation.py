from typing import List, Optional

from pydantic import Field

from pykeadhcp.models.generic.base import KeaModel
from pykeadhcp.models.generic.option_data import OptionData


class Reservation(KeaModel):
    duid: Optional[str] = None
    client_classes: Optional[List[str]] = Field(default_factory=list)
    flex_id: Optional[str] = None
    hw_address: Optional[str] = None
    hostname: Optional[str] = None
    option_data: Optional[List[OptionData]] = Field(default_factory=list)
    subnet_id: Optional[int] = None  # Used for reservation-add
