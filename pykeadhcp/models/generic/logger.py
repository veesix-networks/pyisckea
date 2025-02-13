from typing import Optional, List
from pydantic import Field
from pykeadhcp.models.generic.base import KeaBaseModel, KeaModel
from pykeadhcp.models.enums import LoggerLevelEnum
from typing_extensions import Annotated


class Output(KeaBaseModel):
    output: str
    flush: bool
    maxsize: Optional[int] = None
    maxver: Optional[int] = None
    pattern: Optional[str] = None


class Logger(KeaModel):
    name: str
    output_options: Optional[List[Output]] = Field(default_factory=list)
    debuglevel: Annotated[int, Field(ge=0, le=100)]
    severity: Optional[LoggerLevelEnum] = None
