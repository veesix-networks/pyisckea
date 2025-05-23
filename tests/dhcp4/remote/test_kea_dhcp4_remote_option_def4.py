from pyisckea import Kea
from pyisckea.models.generic.option_def import OptionDef

"""remote-option-def4 process:

get (non existent)
set
get
get-all
del
"""


def test_kea_dhcp4_remote_option_def4_get_non_existent(kea_server: Kea):
    response = kea_server.dhcp4.remote_option_def4_get(
        option_code=1, option_space="pyisckea", server_tag="all"
    )
    assert response.result == 3
    assert response.arguments.get("count") == 0


def test_kea_dhcp4_remote_option_def4_set(kea_server: Kea):
    option_def = OptionDef(name="subopt1", code=1, space="pyisckea", type="string")
    response = kea_server.dhcp4.remote_option_def4_set(
        option_def=option_def, server_tag="all"
    )
    assert response.result == 0
    assert len(response.arguments.get("option-defs", [])) > 0


def test_kea_dhcp4_remote_option_def4_del(kea_server: Kea):
    response = kea_server.dhcp4.remote_option_def4_del(
        option_code=1, option_space="pyisckea", server_tag="all"
    )
    assert response.result == 0
    assert response.arguments.get("count") == 1


def test_kea_dhcp4_remote_option_def4_del_non_existent(kea_server: Kea):
    response = kea_server.dhcp4.remote_option_def4_del(
        option_code=1, option_space="pyisckea", server_tag="all"
    )
    assert response.result == 3
    assert response.arguments.get("count") == 0
