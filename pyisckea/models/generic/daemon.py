from typing import List, Optional

from pydantic import Field

from pyisckea.models.enums import (
    DDNSConflictResolutionModeEnum,
    DHCPSocketTypeEnum,
    HostReservationIdentifierEnum,
    OutboundInterfaceEnum,
)
from pyisckea.models.generic.base import KeaBaseModel
from pyisckea.models.generic.config import CommonDhcpConfig
from pyisckea.models.generic.control_socket import ControlSocket
from pyisckea.models.generic.database import Database
from pyisckea.models.generic.dhcp_ddns import DhcpDdns
from pyisckea.models.generic.dhcp_queue_control import DHCPQueueControl
from pyisckea.models.generic.hook import Hook
from pyisckea.models.generic.logger import Logger
from pyisckea.models.generic.multi_threading import MultiThreading
from pyisckea.models.generic.option_def import OptionDef
from pyisckea.models.generic.sanity_check import SanityCheck


class CommonDaemonConfig(CommonDhcpConfig):
    hooks_libraries: Optional[List[Hook]] = Field(default_factory=list)
    loggers: Optional[List[Logger]] = Field(default_factory=list)


class InterfaceListConfig(KeaBaseModel):
    interfaces: List[str] = Field(default_factory=list)
    dhcp_socket_type: Optional[DHCPSocketTypeEnum] = None
    outbound_interface: Optional[OutboundInterfaceEnum] = None
    re_detect: Optional[bool] = None
    service_sockets_require_all: Optional[bool] = None
    service_sockets_retry_wait_time: Optional[int] = None
    service_sockets_max_retries: Optional[int] = None


class CommonDhcpDaemonConfig(CommonDaemonConfig):
    interfaces_config: InterfaceListConfig
    lease_database: Optional[Database] = None
    hosts_database: Optional[Database] = None
    hosts_databases: Optional[List[Database]] = None
    host_reservation_identifiers: Optional[List[HostReservationIdentifierEnum]] = Field(
        default_factory=list
    )
    option_def: Optional[List[OptionDef]] = Field(default_factory=list)
    expired_leases_processing: Optional[dict] = None
    dhcp4o6_port: Optional[int] = None
    control_socket: Optional[ControlSocket] = None
    ddns_conflict_resolution_mode: Optional[DDNSConflictResolutionModeEnum] = (
        DDNSConflictResolutionModeEnum.check_with_dhcid
    )
    dhcp_queue_control: Optional[DHCPQueueControl] = None
    dhcp_ddns: Optional[DhcpDdns] = None
    sanity_checks: Optional[SanityCheck] = None
    config_control: Optional[dict] = None
    server_tag: Optional[str] = None
    hostname_char_set: Optional[str] = None
    hostname_char_replacement: Optional[str] = None
    statistic_default_sample_count: Optional[int] = None
    statistic_default_sample_age: Optional[int] = None
    multi_threading: Optional[MultiThreading] = None
    early_global_reservations_lookup: Optional[bool] = None
    ip_reservations_unique: Optional[bool] = None
    reservations_lookup_first: Optional[bool] = None
    compatibility: Optional[dict] = None
    parked_packet_limit: Optional[int] = None
    decline_probation_period: Optional[int] = None
    allocator: Optional[str] = None
