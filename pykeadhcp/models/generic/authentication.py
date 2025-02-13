from typing import Optional, List
from pydantic import Field
from pykeadhcp.models.generic.config import CommonConfig
from pykeadhcp.models.enums import AuthenticationTypeEnum


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
