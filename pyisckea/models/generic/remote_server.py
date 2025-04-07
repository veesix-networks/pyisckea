from typing import Optional

from pydantic import StringConstraints
from typing_extensions import Annotated

from pyisckea.models.generic.base import KeaBaseModel


class RemoteServer(KeaBaseModel):
    server_tag: Annotated[str, StringConstraints(max_length=256)]
    description: Optional[str] = None
