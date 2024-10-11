from typing import Optional, List
from pydantic import Field
from pykeadhcp.models.generic.daemon import CommonDhcpDaemonConfig
from pykeadhcp.models.dhcp6.client_class import ClientClass6
from pykeadhcp.models.dhcp6.shared_network import SharedNetwork6
from pykeadhcp.models.dhcp6.subnet import Subnet6
from pykeadhcp.models.dhcp6.reservation import Reservation6
from pykeadhcp.models.dhcp6.server_id import ServerId


class Dhcp6DaemonConfig(CommonDhcpDaemonConfig):
    client_classes: Optional[List[ClientClass6]] = Field(default_factory=list)
    shared_networks: Optional[List[SharedNetwork6]] = Field(default_factory=list)
    reservations: Optional[List[Reservation6]] = Field(default_factory=list)
    data_directory: Optional[str] = None
    preferred_lifetime: Optional[int] = None
    min_preferred_lifetime: Optional[int] = None
    max_preferred_lifetime: Optional[int] = None
    subnet6: Optional[List[Subnet6]] = Field(default_factory=list)
    mac_sources: Optional[List[str]] = Field(default_factory=list)
    relay_supplied_options: Optional[List[str]] = Field(default_factory=list)
    server_id: ServerId
    pd_allocator: Optional[str] = None
