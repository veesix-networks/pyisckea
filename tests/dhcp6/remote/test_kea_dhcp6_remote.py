from pyisckea import Kea
from pyisckea.models.generic.remote_server import RemoteServer

"""remote generic process:
remote-prepare (config backend pull test)
remote-server6-set
remote-server6-get
remote-server6-get (non existent)
remote-server6-get-all
remote-server6-del
"""


def test_kea_dhcp6_remote_prepare(kea_server: Kea):
    response = kea_server.dhcp6.config_backend_pull()
    assert response.result == 0


def test_kea_dhcp6_remote_server6_set(kea_server: Kea):
    response = kea_server.dhcp6.remote_server6_set(
        servers=[RemoteServer(server_tag="pyisckea", description="pyisckea-test")]
    )
    assert response.result == 0


def test_kea_dhcp6_remote_server6_get(kea_server: Kea):
    server = kea_server.dhcp6.remote_server6_get(server_tag="pyisckea")
    assert server
    assert server.server_tag == "pyisckea"
    assert server.description == "pyisckea-test"


def test_kea_dhcp6_remote_server6_get_all(kea_server: Kea, db_remote_map: dict):
    servers = kea_server.dhcp6.remote_server6_get_all(remote_map=db_remote_map)
    assert servers
    assert len(servers) > 0


def test_kea_dhcp6_remote_server6_del(kea_server: Kea):
    response = kea_server.dhcp6.remote_server6_del(servers=["pyisckea"])
    assert response.result == 0
    assert "deleted" in response.text
