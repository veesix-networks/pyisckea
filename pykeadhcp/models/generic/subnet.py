from typing import Optional, List
from pydantic import Field
from pykeadhcp.models.generic.dhcp_common import CommonDHCPParams
from pykeadhcp.models.generic.pool import Pool
from typing_extensions import Annotated


class Subnet(CommonDHCPParams):
    id: Optional[Annotated[int, Field(gt=0, lt=4294967295)]] = None
    pools: Optional[List[Pool]] = []
    subnet: str
    hostname_char_set: Optional[str] = None
    hostname_char_replacement: Optional[str] = None
