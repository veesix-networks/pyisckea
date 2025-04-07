from typing import List, Optional

from pydantic import Field
from typing_extensions import Annotated

from pyisckea.models.generic.dhcp_common import CommonDHCPParams
from pyisckea.models.generic.pool import Pool


# check whether id is still optional with new versions of kea
class Subnet(CommonDHCPParams):
    id: Optional[Annotated[int, Field(gt=0, lt=4294967295)]] = None
    pools: Optional[List[Pool]] = Field(default_factory=list)
    subnet: str
    hostname_char_set: Optional[str] = None
    hostname_char_replacement: Optional[str] = None
    allocator: Optional[str] = None
