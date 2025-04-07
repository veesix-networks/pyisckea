[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![CI Status](https://github.com/BSpendlove/pyisckea/actions/workflows/ci.yml/badge.svg)](https://github.com/BSpendlove/pyisckea/actions/workflows/ci.yml/badge.svg)

#
<p align="center">
  <img src="docs/img/logo.png" alt="Logo" style="max-width: 100%; height: auto; padding-bottom: 8px;">
</p>

<a href="https://github.com/veesix-networks/pyisckea" target="_blank">pyisckea</a> is a python module used to interact with the <a href="https://www.isc.org/kea/" target="_blank">ISC Kea DHCP</a> daemons running on an ISC Kea server. This module also implements <a href="https://docs.pydantic.dev/latest/why/" target="_blank">Pydantic</a> to improve the developer experience when working in a code editor like VSCode and also provide super fast data validation functionality on python objects before they get serialized and sent to the Kea APIs.

## Get Started

1) Install the module.

```
pip install pyisckea
```

2) Import the Kea class.

```python
from pyisckea import Kea

server = Kea("http://localhost:8000")
```

3) Call API commands based on the Daemon to interact with the APIs.

```python
subnets_v4 = server.dhcp4.subnet4_list()

for subnet in subnets_v4:
    print(subnet.subnet, subnet.option_data, subnet.relay, subnet.pools_list)

my_subnet = server.dhcp6.subnet4_get(name="pyisckea-pytest")
print(my_subnet.json(exclude_none=True, indent=4))

# {
#     "valid_lifetime": 4000,
#     "renew_timer": 1000,
#     "rebind_timer": 2000,
#     "option_data": [],
#     "calculate_tee_times": true,
#     "t1_percent": 0.5,
#     "t2_percent": 0.8,
#     "store_extended_info": false,
#     "name": "pyisckea-pytest",
#     "relay": {
#         "ip-addresses": []
#     },
#     "subnet6": [
#         {
#             "valid_lifetime": 4000,
#             "renew_timer": 1000,
#             "rebind_timer": 2000,
#             "option_data": [],
#             "calculate_tee_times": true,
#             "t1_percent": 0.5,
#             "t2_percent": 0.8,
#             "store_extended_info": false,
#             "id": 40123,
#             "subnet": "2001:db8::/64",
#             "preferred_lifetime": 3600,
#             "pd_pools": [],
#             "rapid_commit": false
#         }
#     ],
#     "rapid_commit": false
# }
```

4) Utilize the Pydantic models which provide basic data validation.

```python
from pyisckea.models.dhcp4.subnet import Subnet4

my_subnet = Subnet4(
    id=1234, subnet="192.0.2.32/31", option_data=[{"code": 3, "data": "192.0.2.32"}]
)

create_subnet = server.dhcp4.subnet4_add(subnets=[my_subnet])
print(create_subnet.result, create_subnet.text)

# Note because subnet_cmds hook library is not loaded, we run into an exception here:
# pyisckea.exceptions.KeaHookLibraryNotConfiguredException: Hook library 'subnet_cmds' is not configured for 'dhcp4' service. Please ensure this is enabled in the configuration for the 'dhcp4' daemon
```

## Basic Authentication

If you have basic authentication enabled on your Kea Servers, import the `BasicAuth` class from the `httpx` library and pass it into the `Kea` object like this:

```python
from pyisckea.kea import Kea
from httpx import BasicAuth

auth = BasicAuth("kea", "secret123")


api = Kea("http://localhost:8000", auth=auth)
```

## TLS

Create a context using the `ssl` library and then pass this context into a httpx `Client` object to be used with Kea like this:

```python
from httpx import Client
from pyisckea.kea import Kea

ctx = ssl.create_default_context(cafile="/path/to/the/ca-cert.pem")
ctx.load_cert_chain(
    certfile="/path/to/the/agent-cert.pem", keyfile="/path/to/the/agent-key.pem"
)

client = Client(verify=ctx)
api = Kea("http://localhost:8000", client=client)
```

## API Reference

All supported commands by the daemons are in the format of the API referenced commands with the exception of replacing any hyphen or space with an underscore. Eg. the build-report API command for all daemons is implemented as build_report so it heavily ties into the Kea predefined commands when looking at their documentation. Currently everything is built towards Kea 2.2.0. Pydantic variables will replace any hyphens with an underscore however when loading/exporting the data models, it will replace all keys with the hyphen to adhere to the Kea expected variables, ensure that the KeaBaseModel (located in from pyisckea.models.generic.base import KeaBaseModel instead of from pydantic import BaseModel) is used when creating any Pydantic models to inherit this functionality.