"""The reason why I have created 'remote_reservation' although the API commands are 'reservation-<action>
is because you need a database to use these commands, they don't work with a mem file... Host reservations
must be configured in the global dhcp configuration files as per the documentation:

https://kea.readthedocs.io/en/kea-2.2.0/arm/hooks.html#hooks-host-cmds

"To use the commands that change reservation information (i.e. reservation-add and reservation-del), the hosts database
must be specified and it must not operate in read-only mode
(for details, see the hosts-databases descriptions in DHCPv6 Hosts Database Configuration and DHCPv6 Hosts Database Configuration)."
"""

import pytest

from pyisckea import Kea
from pyisckea.exceptions import KeaException, KeaReservationNotFoundException
from pyisckea.models.dhcp6.subnet import Subnet6

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


def test_kea_dhcp6_remote_reservation_prepare(kea_server: Kea):
    subnet = Subnet6(id=40123, subnet="2001:db8::32/127")
    response = kea_server.dhcp6.remote_subnet6_set(subnet=subnet, server_tags=["all"])
    assert response.result == 0


def test_kea_dhcp6_remote_reservation_get_non_existent(kea_server: Kea):
    with pytest.raises(KeaReservationNotFoundException):
        kea_server.dhcp6.reservation_get_by_identifier(
            subnet_id=40123,
            identifier_type="duid",
            identifier="00:01:00:01:17:96:f9:3a:aa:bb:cc:dd:ee:ff",
        )


def test_kea_dhcp6_remote_reservation_add(kea_server: Kea):
    backend_updated = kea_server.dhcp6.config_backend_pull()
    assert backend_updated.result == 0

    response = kea_server.dhcp6.reservation_add(
        ip_address="2001:db8::33",
        duid="00:01:00:01:17:96:f9:3a:aa:bb:cc:dd:ee:ff",
        hostname="pyisckea-reservation",
        subnet_id=40123,
    )
    assert response.result == 0


def test_kea_dhcp6_remote_reservation_add_existing(kea_server: Kea):
    response = kea_server.dhcp6.reservation_add(
        ip_address="2001:db8::33",
        duid="00:01:00:01:17:96:f9:3a:aa:bb:cc:dd:ee:ff",
        hostname="pyisckea-reservation",
        subnet_id=40123,
    )

    assert response.result == 1


def test_kea_dhcp6_remote_reservation_get_all(kea_server: Kea):
    reservations = kea_server.dhcp6.reservation_get_all(subnet_id=40123)
    assert reservations
    assert len(reservations) > 0


def test_kea_dhcp6_remote_reservation_get_by_ip(kea_server: Kea):
    reservation = kea_server.dhcp6.reservation_get_by_ip_address(
        subnet_id=40123, ip_address="2001:db8::33"
    )
    assert reservation
    assert reservation.hostname == "pyisckea-reservation"
    assert reservation.duid == "00:01:00:01:17:96:f9:3a:aa:bb:cc:dd:ee:ff"
    assert "2001:db8:33" not in [ip for ip in reservation.ip_addresses]


def test_kea_dhcp6_remote_reservation_get_by_hostname(kea_server: Kea):
    hostname = "pyisckea-reservation"
    reservation = kea_server.dhcp6.reservation_get_by_hostname(
        hostname=hostname, subnet_id=40123
    )
    assert reservation
    assert reservation.hostname == hostname


def test_kea_dhcp6_remote_reservation_get_by_identifier(kea_server: Kea):
    duid = "00:01:00:01:17:96:f9:3a:aa:bb:cc:dd:ee:ff"
    reservation = kea_server.dhcp6.reservation_get_by_identifier(
        subnet_id=40123, identifier_type="duid", identifier=duid
    )
    assert reservation
    assert reservation.duid == duid


def test_kea_dhcp6_remote_reservation_get_page(kea_server: Kea):
    reservations = kea_server.dhcp6.reservation_get_page()
    assert reservations
    assert len(reservations) > 0


def test_kea_dhcp6_remote_reservation_get_page_bad_source(kea_server: Kea):
    with pytest.raises(KeaException):
        kea_server.dhcp6.reservation_get_page(source_index=9999)


def test_kea_dhcp6_remote_reservation_del(kea_server: Kea):
    response = kea_server.dhcp6.reservation_del_by_identifier(
        subnet_id=40123,
        identifier_type="duid",
        identifier="00:01:00:01:17:96:f9:3a:aa:bb:cc:dd:ee:ff",
    )
    assert response.result == 0


def test_kea_dhcp6_remote_reservation_cleanup(kea_server: Kea):
    response = kea_server.dhcp6.remote_subnet6_del_by_id(subnet_id=40123)
    assert response.result == 0
