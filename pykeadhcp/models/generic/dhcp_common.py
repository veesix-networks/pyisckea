from typing import Optional, List
from pydantic import Field
from pykeadhcp.models.generic.config import CommonDhcpConfig
from pykeadhcp.models.generic.relay import Relay


class CommonDHCPParams(CommonDhcpConfig):
    """Any param shared between v4/v6 Shared Networks and Subnets"""

    interface: Optional[str] = None
    client_class: Optional[str] = None
    require_client_classes: Optional[List[str]] = Field(default_factory=list)
    relay: Optional[Relay] = None
