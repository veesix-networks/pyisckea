from typing import Optional

from pyisckea.models.enums import NCRFormatEnum, NCRProtocolEnum
from pyisckea.models.generic.config import CommonConfig


class DhcpDdns(CommonConfig):
    enable_updates: bool
    server_ip: str
    server_port: int
    sender_ip: str
    sender_port: int
    max_queue_size: int
    ncr_protocol: NCRProtocolEnum
    ncr_format: NCRFormatEnum
    dep_override_no_update: Optional[bool] = None
    dep_override_client_update: Optional[bool] = None
    dep_replace_client_name: Optional[str] = None
    dep_generated_prefix: Optional[str] = None
    dep_qualifying_suffix: Optional[str] = None
    dep_hostname_char_set: Optional[str] = None
    dep_hostname_char_replacement: Optional[str] = None


"""
"enable-updates": false,
"max-queue-size": 1024,
"ncr-format": "JSON",
"ncr-protocol": "UDP",
"sender-ip": "0.0.0.0",
"sender-port": 0,
"server-ip": "127.0.0.1",
"server-port": 53001
"""
