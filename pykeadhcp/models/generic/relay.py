from typing import List

from pydantic import Field

from pykeadhcp.models.generic.base import KeaBaseModel


class Relay(KeaBaseModel):
    ip_addresses: List[str] = Field(default_factory=list)
