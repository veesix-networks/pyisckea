from typing import Optional
from pykeadhcp.models.generic.config import CommonConfig


class OptionDef(CommonConfig):
    name: str
    code: Optional[int] = None
    type: Optional[str] = None
    record_types: Optional[str] = None
    space: Optional[str] = None
    encapsulate: Optional[str] = None
    array: Optional[bool] = None
