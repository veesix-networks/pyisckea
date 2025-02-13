from typing import Optional, List
from pydantic import ConfigDict, BaseModel, Field
from pykeadhcp.models.enums import StatusEnum


class Sockets(BaseModel):
    errors: Optional[List[str]] = Field(default_factory=list)
    status: StatusEnum
    model_config = ConfigDict(use_enum_values=True)
