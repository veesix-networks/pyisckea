from typing import Annotated, List, Optional

from pydantic import ConfigDict, Field

from pyisckea.models.dhcp4.reservation import Reservation4
from pyisckea.models.generic.subnet import Subnet


class Subnet4(Subnet):
    match_client_id: Optional[bool] = None
    authoritative: Optional[bool] = None
    next_server: Optional[str] = None
    boot_file_name: Optional[str] = None
    subnet_4o6_interface: Annotated[Optional[str], Field(alias="4o6-interface")] = None
    subnet_4o6_interface_id: Annotated[
        Optional[str], Field(alias="4o6-interface-id")
    ] = None
    subnet_4o6_subnet: Annotated[Optional[str], Field(alias="4o6-subnet")] = None
    reservations: Optional[List[Reservation4]] = Field(default_factory=list)

    model_config = ConfigDict(populate_by_name=True)
