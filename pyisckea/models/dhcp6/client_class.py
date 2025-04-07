from typing import Optional

from pyisckea.models.generic.client_class import ClientClass


class ClientClass6(ClientClass):
    preferred_lifetime: Optional[int] = None
    min_preferred_lifetime: Optional[int] = None
    max_preferred_lifetime: Optional[int] = None
