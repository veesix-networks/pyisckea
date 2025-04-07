from pyisckea import Kea

"""remote-global-parameter4 process:

get (non existent)
set
get
get-all
del
"""


def test_kea_dhcp4_remote_global_parameter4_get_non_existent(kea_server: Kea):
    response = kea_server.dhcp4.remote_global_parameter4_get(
        parameter="boot-file-name", server_tag="pyisckea-1"
    )
    assert response.result == 3
    assert response.arguments.get("count") == 0


def test_kea_dhcp4_remote_global_parameter4_set(kea_server: Kea):
    response = kea_server.dhcp4.remote_global_parameter4_set(
        parameters={"boot-file-name": "/dev/null"}, server_tag="all"
    )
    assert response.result == 0
    assert response.arguments.get("count") == 1


def test_kea_dhcp4_remote_global_parameter4_get(kea_server: Kea):
    response = kea_server.dhcp4.remote_global_parameter4_get(
        parameter="boot-file-name", server_tag="all"
    )
    assert response.result == 0
    assert response.arguments.get("count") == 1


def test_kea_dhcp4_remote_global_parameter4_get_all(kea_server: Kea):
    response = kea_server.dhcp4.remote_global_parameter4_get_all(server_tag="all")
    assert response.result == 0
    assert len(response.arguments.get("parameters")) > 0


def test_kea_dhcp4_remote_global_parameter4_del(kea_server: Kea):
    response = kea_server.dhcp4.remote_global_parameter4_del(
        parameter="boot-file-name", server_tag="all"
    )
    assert response.result == 0


def test_kea_dhcp4_remote_global_parameter4_del_non_existent(kea_server: Kea):
    response = kea_server.dhcp4.remote_global_parameter4_del(
        parameter="boot-file-name", server_tag="all"
    )
    assert response.result == 3
