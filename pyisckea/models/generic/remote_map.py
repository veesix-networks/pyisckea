from typing import Optional

from pydantic import Field
from typing_extensions import Annotated

from pyisckea.models.enums import RemoteMapTypeEnum
from pyisckea.models.generic.base import KeaBaseModel


class RemoteMap(KeaBaseModel):
    type: Optional[RemoteMapTypeEnum] = None
    host: Optional[str] = None
    port: Optional[Annotated[int, Field(gt=1, le=65535)]] = None
