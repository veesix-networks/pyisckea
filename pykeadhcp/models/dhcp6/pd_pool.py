from typing import List, Optional

from pydantic import Field

from pykeadhcp.models.generic.base import KeaModel
from pykeadhcp.models.generic.option_data import OptionData


class PDPool(KeaModel):
    prefix: str
    prefix_len: int
    delegated_len: int
    option_data: Optional[List[OptionData]] = Field(default_factory=list)
    client_class: Optional[str] = None
    require_client_classes: Optional[List[str]] = Field(default_factory=list)
    excluded_prefix: Optional[str] = None
    excluded_prefix_len: Optional[int] = None
