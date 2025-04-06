from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from pykeadhcp.models.enums import StatusEnum


class Sockets(BaseModel):
    errors: Optional[List[str]] = Field(default_factory=list)
    status: StatusEnum
    model_config = ConfigDict(use_enum_values=True)
