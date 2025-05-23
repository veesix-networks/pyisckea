"""The reason why I have created 'remote_reservation' although the API commands are 'reservation-<action>
is because you need a database to use these commands, they don't work with a mem file... Host reservations
must be configured in the global dhcp configuration files as per the documentation:

https://kea.readthedocs.io/en/kea-2.2.0/arm/hooks.html#hooks-host-cmds

"To use the commands that change reservation information (i.e. reservation-add and reservation-del), the hosts database
must be specified and it must not operate in read-only mode
(for details, see the hosts-databases descriptions in DHCPv4 Hosts Database Configuration and DHCPv6 Hosts Database Configuration)."
"""

import pytest

from pyisckea import Kea
from pyisckea.exceptions import KeaException, KeaReservationNotFoundException
from pyisckea.models.dhcp4.subnet import Subnet4

"""reservation process:
reservation-get non existent
reservation-add
reservation-add existing
reservation-get-all
reservation-get
reservation-get-by-hostname
reservation-get-by-id
reservation-get-page
reservation-del
reservation-del non existent
"""


def test_kea_dhcp4_remote_reservation_prepare(kea_server: Kea):
    subnet = Subnet4(id=40123, subnet="192.0.2.32/31")
    response = kea_server.dhcp4.remote_subnet4_set(subnet=subnet, server_tags=["all"])
    assert response.result == 0


def test_kea_dhcp4_remote_reservation_get_non_existent(kea_server: Kea):
    with pytest.raises(KeaReservationNotFoundException):
        kea_server.dhcp4.reservation_get_by_identifier(
            subnet_id=40123,
            identifier_type="hw-address",
            identifier="aa:bb:cc:dd:ee:ff",
        )


def test_kea_dhcp4_remote_reservation_add(kea_server: Kea):
    backend_updated = kea_server.dhcp4.config_backend_pull()
    assert backend_updated.result == 0

    response = kea_server.dhcp4.reservation_add(
        ip_address="192.0.2.33",
        hw_address="aa:bb:cc:dd:ee:ff",
        hostname="pyisckea-reservation",
        subnet_id=40123,
    )
    assert response.result == 0


def test_kea_dhcp4_remote_reservation_add_existing(kea_server: Kea):
    response = kea_server.dhcp4.reservation_add(
        ip_address="192.0.2.33",
        hw_address="aa:bb:cc:dd:ee:ff",
        hostname="pyisckea-reservation",
        subnet_id=40123,
    )

    assert response.result == 1


def test_kea_dhcp4_remote_reservation_get_all(kea_server: Kea):
    reservations = kea_server.dhcp4.reservation_get_all(subnet_id=40123)
    assert reservations
    assert len(reservations) > 0


def test_kea_dhcp4_remote_reservation_get_by_ip(kea_server: Kea):
    reservation = kea_server.dhcp4.reservation_get_by_ip_address(
        subnet_id=40123, ip_address="192.0.2.33"
    )
    assert reservation
    assert reservation.hostname == "pyisckea-reservation"
    assert reservation.hw_address == "aa:bb:cc:dd:ee:ff"
    assert reservation.ip_address == "192.0.2.33"


def test_kea_dhcp4_remote_reservation_get_by_hostname(kea_server: Kea):
    hostname = "pyisckea-reservation"
    reservation = kea_server.dhcp4.reservation_get_by_hostname(
        hostname=hostname, subnet_id=40123
    )
    assert reservation
    assert reservation.hostname == hostname


def test_kea_dhcp4_remote_reservation_get_by_identifier(kea_server: Kea):
    hw_address = "aa:bb:cc:dd:ee:ff"
    reservation = kea_server.dhcp4.reservation_get_by_identifier(
        subnet_id=40123, identifier_type="hw-address", identifier=hw_address
    )
    assert reservation
    assert reservation.hw_address == hw_address


def test_kea_dhcp4_remote_reservation_get_page(kea_server: Kea):
    reservations = kea_server.dhcp4.reservation_get_page()
    assert reservations
    assert len(reservations) > 0


def test_kea_dhcp4_remote_reservation_get_page_bad_source(kea_server: Kea):
    with pytest.raises(KeaException):
        kea_server.dhcp4.reservation_get_page(source_index=9999)


def test_kea_dhcp4_remote_reservation_del(kea_server: Kea):
    response = kea_server.dhcp4.reservation_del_by_ip(
        subnet_id=40123, ip_address="192.0.2.33"
    )
    assert response.result == 0


def test_kea_dhcp4_remote_reservation_cleanup(kea_server: Kea):
    response = kea_server.dhcp4.remote_subnet4_del_by_id(subnet_id=40123)
    assert response.result == 0
