from typing import Optional

from pyisckea.models.generic.reservation import Reservation


class Reservation4(Reservation):
    client_id: Optional[str] = None
    circuit_id: Optional[str] = None
    ip_address: str
    next_server: Optional[str] = None
    server_hostname: Optional[str] = None
    boot_file_name: Optional[str] = None
