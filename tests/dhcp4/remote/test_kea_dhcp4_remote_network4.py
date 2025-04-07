import pytest

from pyisckea import Kea
from pyisckea.exceptions import KeaSharedNetworkNotFoundException
from pyisckea.models.dhcp4.shared_network import SharedNetwork4
from pyisckea.models.dhcp4.subnet import Subnet4

"""remote-network4 process:
get (non-existent network)
add
list
get
add and delete subnet (for existing shared-network)
del
del (non-existent)
"""


def test_kea_dhcp4_remote_network4_get_non_existent(kea_server: Kea):
    name = "pykeadhcp-pytest"
    with pytest.raises(KeaSharedNetworkNotFoundException):
        kea_server.dhcp4.remote_network4_get(name=name)


def test_kea_dhcp4_remote_network4_add(kea_server: Kea, db_remote_map: dict):
    name = "pykeadhcp-pytest"
    data = SharedNetwork4(name=name)
    shared_networks = [data]
    response = kea_server.dhcp4.remote_network4_set(
        shared_networks=shared_networks, server_tags=["all"], remote_map=db_remote_map
    )

    assert response.result == 0
    assert len(response.arguments.get("shared-networks", [])) > 0


def test_kea_dhcp4_remote_network4_list(kea_server: Kea, db_remote_map: dict):
    shared_networks = kea_server.dhcp4.remote_network4_list(
        server_tags=["pykeadhcp-1"], remote_map=db_remote_map
    )
    assert shared_networks
    assert len(shared_networks) > 0


def test_kea_dhcp4_remote_network4_get(kea_server: Kea, db_remote_map: dict):
    name = "pykeadhcp-pytest"
    shared_network = kea_server.dhcp4.remote_network4_get(
        name=name, remote_map=db_remote_map
    )
    assert shared_network
    assert shared_network.name == name


def test_kea_dhcp4_remote_subnet4_add_subnet(kea_server: Kea, db_remote_map: dict):
    name = "pykeadhcp-pytest"

    # Create Temporary Subnet
    subnet = Subnet4(subnet="192.0.2.32/31", id=40123, shared_network_name=name)

    # Create subnet with shared network assosication
    response = kea_server.dhcp4.remote_subnet4_set(
        subnet=subnet, server_tags=["all"], remote_map=db_remote_map
    )
    assert response.result == 0
    assert len(response.arguments.get("subnets", [])) > 0


def test_kea_dhcp4_remote_subnet4_del_by_id(kea_server: Kea, db_remote_map: dict):
    response = kea_server.dhcp4.remote_subnet4_del_by_id(
        subnet_id=40123, remote_map=db_remote_map
    )
    assert response.result == 0
    assert response.arguments.get("count") == 1


def test_kea_dhcp4_remote_network4_del(kea_server: Kea, db_remote_map: dict):
    response = kea_server.dhcp4.remote_network4_del(
        name="pykeadhcp-pytest", keep_subnets=False, remote_map=db_remote_map
    )
    assert response.result == 0
    assert response.arguments.get("count") == 1


def test_kea_dhcp4_remote_network4_del_non_existent(
    kea_server: Kea, db_remote_map: dict
):
    response = kea_server.dhcp4.remote_network4_del(
        name="pykeadhcp-pytest", remote_map=db_remote_map
    )
    assert response.result == 3
    assert response.arguments["count"] == 0
