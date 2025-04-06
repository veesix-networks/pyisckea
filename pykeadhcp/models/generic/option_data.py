from typing import Optional

from pykeadhcp.models.generic.base import KeaModel


class OptionData(KeaModel):
    data: str
    name: Optional[str] = None
    code: Optional[int] = None
    space: Optional[str] = None
    csv_format: Optional[bool] = None
    always_send: Optional[bool] = None
    never_send: Optional[bool] = None
