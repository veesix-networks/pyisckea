from typing import List, Optional

from pydantic import Field

from pyisckea.models.generic.base import KeaModel
from pyisckea.models.generic.option_data import OptionData


class Pool(KeaModel):
    pool: str
    option_data: Optional[List[OptionData]] = Field(default_factory=list)
    client_class: Optional[str] = None
    require_client_classes: Optional[str] = None
