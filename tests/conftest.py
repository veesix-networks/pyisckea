import json
from pathlib import Path
from httpx import BasicAuth

import pytest
from pytest import FixtureRequest

from pyisckea import Kea
from pyisckea.models.ctrlagent.config import CtrlAgentDaemonConfig
from pyisckea.models.dhcp4.config import Dhcp4DaemonConfig
from pyisckea.models.dhcp6.config import Dhcp6DaemonConfig
from pyisckea.parsers import CtrlAgentParser, Dhcp4Parser, Dhcp6Parser


def pytest_addoption(parser):
    parser.addoption(
        "--kea-host",
        action="store",
        dest="kea_host",
        type=str,
        help="URL for Kea Server API",
        default="http://127.0.0.1:8000",
    )
    parser.addoption(
        "--basic-auth",
        action="store_true",
        dest="basic_auth",
        default=True,
        help="Use BasicAuth for Kea Server API",
    )
    parser.addoption(
        "--username",
        action="store",
        dest="username",
        type=str,
        help="Username for BasicAuth for Kea Server API",
        default="kea",
    )
    parser.addoption(
        "--password",
        action="store",
        dest="password",
        type=str,
        help="Password for BasicAuth for Kea Server API",
        default="secret123",
    )
    parser.addoption(
        "--disable-ssl-verify",
        action="store_true",
        dest="disable_ssl_verify",
        default=False,
        help="Disable SSL Verification when calling Kea class",
    )
    parser.addoption(
        "--ssl-ca-bundle",
        action="store",
        dest="ssl_ca_bundle",
        type=str,
        help="CA Bundle if required to pass into requests module",
        default=None,
    )
    parser.addoption(
        "--db-type",
        action="store",
        dest="db_type",
        type=str,
        help="Database Type to set in the remote_map to all API calls starting with 'remote'",
        default="mysql",
    )
    parser.addoption(
        "--db-host",
        action="store",
        dest="db_host",
        type=str,
        help="Database Host to set in the remote_map to all API calls starting with 'remote'",
        default="db",
    )
    parser.addoption(
        "--raise-generic-errors",
        action="store_true",
        dest="raise_generic_errors",
        default=False,
        help="Raise Generic Kea Errors (useful for catching errors when developing)",
    )


@pytest.fixture(scope="module")
def kea_server(request: FixtureRequest):
    kea_host = request.config.getoption("kea_host")
    use_basic_auth = request.config.getoption("basic_auth", default=True)
    username = request.config.getoption("username")
    password = request.config.getoption("password")
    disable_ssl_verify = request.config.getoption("disable_ssl_verify", default=False)
    ssl_ca_bundle = request.config.getoption("ssl_ca_bundle", default=None)
    raise_generic_errors = request.config.getoption(
        "raise_generic_errors", default=False
    )

    return Kea(
        kea_host=kea_host,
        auth=BasicAuth(username, password) if use_basic_auth else None,
        raise_generic_errors=raise_generic_errors,
        verify=(
            False
            if disable_ssl_verify
            else True
            if not ssl_ca_bundle
            else ssl_ca_bundle
        ),
    )


def read_local_config(filename: str):
    json_file = Path(filename)
    if not json_file.exists():
        raise FileNotFoundError

    with json_file.open() as config:
        return json.load(config)


@pytest.fixture(scope="module")
def ctrlagent_model(request: FixtureRequest):
    data = read_local_config(filename="tests/configs/ctrlagent_api_config.json")
    assert data["Control-agent"]
    return CtrlAgentDaemonConfig.model_validate(data["Control-agent"])


@pytest.fixture(scope="module")
def dhcp4_model(request: FixtureRequest):
    data = read_local_config(filename="tests/configs/dhcp4_api_config.json")
    assert data["Dhcp4"]
    return Dhcp4DaemonConfig.model_validate(data["Dhcp4"])


@pytest.fixture(scope="module")
def dhcp6_model(request: FixtureRequest):
    data = read_local_config(filename="tests/configs/dhcp6_api_config.json")
    assert data["Dhcp6"]
    return Dhcp6DaemonConfig.model_validate(data["Dhcp6"])


@pytest.fixture(scope="module")
def dhcp4_parser(request: FixtureRequest):
    data = read_local_config(filename="tests/configs/dhcp4_api_config.json")
    assert data["Dhcp4"]
    return Dhcp4Parser(config=data)


@pytest.fixture(scope="module")
def dhcp6_parser(request: FixtureRequest):
    data = read_local_config(filename="tests/configs/dhcp6_api_config.json")
    assert data["Dhcp6"]
    return Dhcp6Parser(config=data)


@pytest.fixture(scope="module")
def ctrlagent_parser(request: FixtureRequest):
    data = read_local_config(filename="tests/configs/ctrlagent_api_config.json")
    assert data["Control-agent"]
    return CtrlAgentParser(config=data)


@pytest.fixture(scope="module")
def db_remote_map(request: FixtureRequest):
    return {
        "type": request.config.getoption("db_type"),
        "host": request.config.getoption("db_host"),
    }
