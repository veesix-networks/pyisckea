from typing import List, Optional

from pydantic import Field

from pyisckea.models.dhcp4.subnet import Subnet4
from pyisckea.models.generic.shared_network import SharedNetwork


class SharedNetwork4(SharedNetwork):
    subnet4: Optional[List[Subnet4]] = Field(default_factory=list)
    match_client_id: Optional[bool] = None
    authoritative: Optional[bool] = None
    next_server: Optional[str] = None
    server_hostname: Optional[str] = None
    boot_file_name: Optional[str] = None
