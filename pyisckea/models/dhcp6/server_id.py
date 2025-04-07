from typing import Optional

from pyisckea.models.enums import ServerIdTypeEnum
from pyisckea.models.generic.config import CommonConfig


class ServerId(CommonConfig):
    type: ServerIdTypeEnum
    htype: int
    identifier: Optional[str] = None
    time: int
    enterprise_id: int
    persist: bool
