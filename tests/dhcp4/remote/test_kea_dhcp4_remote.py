from pyisckea import Kea
from pyisckea.models.generic.remote_server import RemoteServer

"""remote generic process:
remote-prepare (config backend pull test)
remote-server4-set
remote-server4-get
remote-server4-get (non existent)
remote-server4-get-all
remote-server4-del
"""


def test_kea_dhcp4_remote_prepare(kea_server: Kea):
    response = kea_server.dhcp4.config_backend_pull()
    assert response.result == 0


def test_kea_dhcp4_remote_server4_set(kea_server: Kea):
    response = kea_server.dhcp4.remote_server4_set(
        servers=[RemoteServer(server_tag="pyisckea", description="pyisckea-test")]
    )
    assert response.result == 0


def test_kea_dhcp4_remote_server4_get(kea_server: Kea):
    server = kea_server.dhcp4.remote_server4_get(server_tag="pyisckea")
    assert server
    assert server.server_tag == "pyisckea"
    assert server.description == "pyisckea-test"


def test_kea_dhcp4_remote_server4_del(kea_server: Kea):
    response = kea_server.dhcp4.remote_server4_del(servers=["pyisckea"])
    assert response.result == 0
    assert "deleted" in response.text
