from typing import Optional

from pyisckea.models.generic.dhcp_common import CommonDHCPParams


class SharedNetwork(CommonDHCPParams):
    name: str
    relay: Optional[dict] = None
