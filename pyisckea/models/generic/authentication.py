from typing import List, Optional

from pydantic import Field

from pyisckea.models.enums import AuthenticationTypeEnum
from pyisckea.models.generic.config import CommonConfig


class AuthenticationClient(CommonConfig):
    user: Optional[str] = None
    user_file: Optional[str] = None
    password: Optional[str] = None
    password_file: Optional[str] = None


class Authentication(CommonConfig):
    type: AuthenticationTypeEnum
    realm: str
    directory: Optional[str] = None
    clients: List[Optional[AuthenticationClient]] = Field(default_factory=list)
