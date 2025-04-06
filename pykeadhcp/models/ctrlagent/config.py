from typing import Optional
from pykeadhcp.models.generic.daemon import CommonDaemonConfig
from pykeadhcp.models.generic.control_socket import ControlSockets


class CtrlAgentDaemonConfig(CommonDaemonConfig):
    http_host: str
    http_port: int
    trust_anchor: Optional[str] = None
    cert_file: Optional[str] = None
    key_file: Optional[str] = None
    cert_required: Optional[bool] = None
    control_sockets: Optional[ControlSockets] = None
    authentication: Optional[dict] = None
