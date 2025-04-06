from typing import List, Union

from pykeadhcp.models.enums import HAModeTypeEnum, HARoleTypeEnum, HAStateTypeEnum
from pykeadhcp.models.generic.base import KeaBaseModel


class HAServerLocal(KeaBaseModel):
    role: HARoleTypeEnum
    scopes: List[str]
    state: HAStateTypeEnum


class HAServerRemote(KeaBaseModel):
    age: int
    in_touch: bool
    last_scopes: List[str]
    last_state: Union[None, HAStateTypeEnum] = None
    role: HARoleTypeEnum


class HAServers(KeaBaseModel):
    local: HAServerLocal
    remote: HAServerRemote


class HighAvailability(KeaBaseModel):
    ha_mode: HAModeTypeEnum
    ha_servers: HAServers
