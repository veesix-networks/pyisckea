from typing import List, Optional

from pydantic import Field
from typing_extensions import Annotated

from pyisckea.models.enums import LoggerLevelEnum
from pyisckea.models.generic.base import KeaBaseModel, KeaModel


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
