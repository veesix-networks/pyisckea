from typing import Optional, List
from pykeadhcp.models.generic.base import KeaModel
from pykeadhcp.models.generic.option_data import OptionData


class Reservation(KeaModel):
    duid: Optional[str] = None
    client_classes: Optional[List[str]] = []
    flex_id: Optional[str] = None
    hw_address: Optional[str] = None
    hostname: Optional[str] = None
    option_data: Optional[List[OptionData]] = []
    subnet_id: Optional[int] = None  # Used for reservation-add
