from typing import Any, List, Optional, TYPE_CHECKING
from pydantic import BaseModel

from pykeadhcp.models.generic.shared_network import SharedNetwork
from pykeadhcp.models.dhcp4.subnet import Subnet4


class SharedNetwork4(SharedNetwork):
    subnet4: Optional[List[Subnet4]] = []
    match_client_id: Optional[bool] = None
    authoritative: Optional[bool] = None
    next_server: Optional[str] = None
    server_hostname: Optional[str] = None
    boot_file_name: Optional[str] = None
