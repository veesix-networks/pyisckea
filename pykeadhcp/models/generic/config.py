from typing import Optional, List, Union
from pydantic import Field
from pykeadhcp.models.generic.base import KeaModel
from pykeadhcp.models.generic.option_data import OptionData
from pykeadhcp.models.enums import ReservationMode, DDNSReplaceClientNameEnum


class CommonConfig(KeaModel):
    store_extended_info: Optional[bool] = None


class CommonDhcpConfig(CommonConfig):
    valid_lifetime: Optional[int] = None
    min_valid_lifetime: Optional[int] = None
    max_valid_lifetime: Optional[int] = None
    renew_timer: Optional[int] = None
    rebind_timer: Optional[int] = None
    option_data: Optional[List[OptionData]] = Field(default_factory=list)
    reservation_mode: Optional[ReservationMode] = None
    reservations_global: Optional[bool] = None
    reservations_in_subnet: Optional[bool] = None
    reservations_out_of_pool: Optional[bool] = None
    calculate_tee_times: Optional[bool] = None
    t1_percent: Optional[float] = None
    t2_percent: Optional[float] = None
    cache_threshold: Optional[float] = None
    cache_max_age: Optional[int] = None
    ddns_send_updates: Optional[bool] = None
    ddns_override_no_update: Optional[bool] = None
    ddns_override_client_update: Optional[bool] = None
    ddns_replace_client_name: Optional[Union[DDNSReplaceClientNameEnum, bool]] = None
    ddns_generated_prefix: Optional[str] = None
    ddns_qualifying_suffix: Optional[str] = None
    ddns_update_on_renew: Optional[bool] = None
    ddns_use_conflict_resolution: Optional[bool] = None
