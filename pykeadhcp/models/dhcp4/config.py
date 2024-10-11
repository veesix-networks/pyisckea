from typing import Optional, List
from pydantic import Field
from pykeadhcp.models.generic.daemon import CommonDhcpDaemonConfig
from pykeadhcp.models.dhcp4.client_class import ClientClass4
from pykeadhcp.models.dhcp4.shared_network import SharedNetwork4
from pykeadhcp.models.dhcp4.subnet import Subnet4
from pykeadhcp.models.dhcp4.reservation import Reservation4


class Dhcp4DaemonConfig(CommonDhcpDaemonConfig):
    client_classes: Optional[List[ClientClass4]] = Field(default_factory=list)
    shared_networks: Optional[List[SharedNetwork4]] = Field(default_factory=list)
    reservations: Optional[List[Reservation4]] = Field(default_factory=list)
    subnet4: Optional[List[Subnet4]] = Field(default_factory=list)
    echo_client_id: Optional[bool] = None
    match_client_id: Optional[bool] = None
    authoritative: Optional[bool] = None
    next_server: Optional[str] = None
    server_hostname: Optional[str] = None
    boot_file_name: Optional[str] = None
