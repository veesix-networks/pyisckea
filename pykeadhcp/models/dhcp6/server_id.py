from typing import Optional
from pykeadhcp.models.generic.config import CommonConfig
from pykeadhcp.models.enums import ServerIdTypeEnum


class ServerId(CommonConfig):
    type: ServerIdTypeEnum
    htype: int
    identifier: Optional[str] = None
    time: int
    enterprise_id: int
    persist: bool
