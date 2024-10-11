from typing import Optional
from pydantic import Field
from pykeadhcp.models.generic.base import KeaBaseModel
from pykeadhcp.models.enums import RemoteMapTypeEnum
from typing_extensions import Annotated


class RemoteMap(KeaBaseModel):
    type: Optional[RemoteMapTypeEnum] = None
    host: Optional[str] = None
    port: Optional[Annotated[int, Field(gt=1, le=65535)]] = None
