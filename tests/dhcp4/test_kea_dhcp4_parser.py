import json

from pyisckea import Kea
from pyisckea.parsers.dhcp4 import Dhcp4Parser


def test_kea_dhcp4_parser_parse_config(kea_server: Kea):
    cached_config = kea_server.dhcp4.cached_config
    parsed = Dhcp4Parser(config=cached_config)

    assert parsed.config.interfaces_config
    assert parsed.config.control_socket
    assert json.dumps(
        parsed.config.model_dump(exclude_none=True, by_alias=True),
        indent=4,
        sort_keys=True,
    )


def test_kea_dhcp4_parser_config_test(kea_server: Kea):
    cached_config = kea_server.dhcp4.cached_config
    parsed = Dhcp4Parser(config=cached_config)
    config_to_test = {
        "Dhcp4": parsed.config.model_dump(
            exclude_none=True, exclude_unset=True, by_alias=True
        )
    }

    test_results = kea_server.dhcp4.config_test(config=config_to_test)
    assert test_results.result == 0

    # Remove hash if exist for now until tests are created to take that into account
    if cached_config.get("hash"):
        del cached_config["hash"]

    cached_config_json = json.dumps(cached_config, indent=4)
    parsed_config_json = json.dumps(config_to_test, indent=4, sort_keys=True)
    assert cached_config_json == parsed_config_json
