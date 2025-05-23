import pytest

from pyisckea import Kea
from pyisckea.exceptions import KeaClientClassNotFoundException
from pyisckea.models.dhcp6.client_class import ClientClass6

"""class process:class_del
get (non-existent client-class)
add
add (again to check duplicate client-class)
get
list
update
del
del (non-existent client-class)
"""


def test_kea_dhcp6_class_get_non_existent(kea_server: Kea):
    with pytest.raises(KeaClientClassNotFoundException):
        kea_server.dhcp6.class_get(name="ipxe_efi_x64")


def test_kea_dhcp6_class_add(kea_server: Kea):
    client_class = ClientClass6(
        name="ipxe_efi_x64",
        test="option[93].hex == 0x0009",
        next_server="192.0.2.254",
        server_hostname="hal9000",
        boot_file_name="/dev/null",
    )
    response = kea_server.dhcp6.class_add(client_class=client_class)
    assert response.result == 0


def test_kea_dhcp6_class_get(kea_server: Kea):
    response = kea_server.dhcp6.class_get(name="ipxe_efi_x64")
    assert response
    assert response.name == "ipxe_efi_x64"


def test_kea_dhcp6_class_list(kea_server: Kea):
    response = kea_server.dhcp6.class_list()
    assert len(response) > 0


def test_kea_dhcp6_class_del(kea_server: Kea):
    response = kea_server.dhcp6.class_del(name="ipxe_efi_x64")
    assert response.result == 0


def test_kea_dhcp6_class_del_non_existent(kea_server: Kea):
    response = kea_server.dhcp6.class_del(name="ipxe_efi_x64")
    assert response.result == 3
