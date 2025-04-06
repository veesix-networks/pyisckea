from typing import List, Optional

from pykeadhcp.models.generic.config import CommonConfig
from pykeadhcp.models.generic.option_data import OptionData


class ClientClass(CommonConfig):
    name: str
    test: Optional[str] = None
    only_if_required: Optional[bool] = None
    option_data: Optional[List[OptionData]] = None
    valid_lifetime: Optional[int] = None
    min_valid_lifetime: Optional[int] = None
    max_valid_lifetime: Optional[int] = None
