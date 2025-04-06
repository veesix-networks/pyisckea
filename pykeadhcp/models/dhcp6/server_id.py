from typing import Optional

from pykeadhcp.models.enums import ServerIdTypeEnum
from pykeadhcp.models.generic.config import CommonConfig


class ServerId(CommonConfig):
    type: ServerIdTypeEnum
    htype: int
    identifier: Optional[str] = None
    time: int
    enterprise_id: int
    persist: bool
