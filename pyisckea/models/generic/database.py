from typing import Optional

from pyisckea.models.enums import DatabaseOnFailEnum, DatabaseTypeEnum
from pyisckea.models.generic.base import KeaBaseModel


class Database(KeaBaseModel):
    type: DatabaseTypeEnum
    user: Optional[str] = None
    password: Optional[str] = None
    host: Optional[str] = None
    port: Optional[int] = None
    name: Optional[str] = None
    persist: Optional[bool] = None
    lfc_interval: Optional[int] = None
    readonly: Optional[bool] = None
    connect_timeout: Optional[int] = None
    max_reconnect_tries: Optional[int] = None
    on_fail: Optional[DatabaseOnFailEnum] = None
    max_row_errors: Optional[int] = None
    trust_anchor: Optional[str] = None
    cert_file: Optional[str] = None
    key_file: Optional[str] = None
    cipher_list: Optional[str] = None
    unknown_map_entry: Optional[str] = None
