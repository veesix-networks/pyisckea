from typing import Optional

from pyisckea.models.generic.base import KeaBaseModel


class Lease(KeaBaseModel):
    cltt: Optional[int] = None
    fqdn_fwd: Optional[bool] = None
    fqdn_rev: Optional[bool] = None
    hostname: Optional[str] = None
    hw_address: Optional[str] = None
    ip_address: str
    state: Optional[int] = None
    subnet_id: Optional[int] = None
    valid_lft: Optional[int] = None


class LeasePage(KeaBaseModel):
    count: int
