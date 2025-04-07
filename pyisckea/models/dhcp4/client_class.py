from typing import List, Optional

from pydantic import Field

from pyisckea.models.generic.client_class import ClientClass
from pyisckea.models.generic.option_def import OptionDef


class ClientClass4(ClientClass):
    option_def: Optional[List[OptionDef]] = Field(default_factory=list)
    next_server: Optional[str] = None
    server_hostname: Optional[str] = None
    boot_file_name: Optional[str] = None
