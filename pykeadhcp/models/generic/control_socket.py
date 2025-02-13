from typing import Optional
from pykeadhcp.models.generic.base import KeaBaseModel
from pykeadhcp.models.generic.config import CommonConfig


class ControlSocket(CommonConfig):
    socket_name: str
    socket_type: str


class ControlSockets(KeaBaseModel):
    dhcp4: Optional[ControlSocket] = None
    dhcp6: Optional[ControlSocket] = None
    d2: Optional[ControlSocket] = None
    unknown_map_entry: Optional[str] = None
