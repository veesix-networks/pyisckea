from typing import Optional
from pydantic import ConfigDict, BaseModel


def normalize_keys(string: str) -> str:
    return string.replace("_", "-")


class KeaBaseModel(BaseModel):
    model_config = ConfigDict(
        alias_generator=normalize_keys, populate_by_name=True, use_enum_values=True
    )


class KeaModel(KeaBaseModel):
    user_context: Optional[dict] = None
    comment: Optional[str] = None
    unknown_map_entry: Optional[str] = None
