from typing import Optional
from pydantic import StringConstraints
from pykeadhcp.models.generic.base import KeaBaseModel
from typing_extensions import Annotated


class RemoteServer(KeaBaseModel):
    server_tag: Annotated[str, StringConstraints(max_length=256)]
    description: Optional[str] = None
