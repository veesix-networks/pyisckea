from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pykeadhcp import Kea


class CtrlAgent:
    def __init__(self, api: "Kea"):
        self.service = None  # Control Agent expects service: [] in payload
        self.api = api

    def build_report(self) -> dict:
        """Returns list of compilation options that this particular binary was built with

        Kea API Reference:
            https://kea.readthedocs.io/en/kea-2.2.0/api.html#ref-build-report
        """
        return self.api.send_command(command="build-report", service=self.service)

    def config_get(self) -> dict:
        """Retrieves the current configuration used by the server

        Kea API Reference:
            https://kea.readthedocs.io/en/kea-2.2.0/api.html#ref-config-get
        """
        return self.api.send_command(command="config-get", service=self.service)

    def config_reload(self) -> dict:
        """Reloads the last good configuration (configuration file on disk)

        Kea API Reference:
            https://kea.readthedocs.io/en/kea-2.2.0/api.html#ref-config-reload
        """
        return self.api.send_command(command="config-reload", service=self.service)

    def config_set(self, config: dict) -> dict:
        """Replace the current server configuration with the provided configuration

        Args:
            config:     Configuration to set

        Kea API Reference:
            https://kea.readthedocs.io/en/kea-2.2.0/api.html#config-set
        """
        return self.api.send_command_with_arguments(
            command="config-set", service=self.service, arguments=config
        )

    def config_test(self, config: dict) -> dict:
        """Check whether the configuration supplied can be loaded by the dhcp4 daemon

        Args:
            config:     Configuration to test

        Kea API Reference:
            https://kea.readthedocs.io/en/kea-2.2.0/api.html#config-test
        """
        return self.api.send_command_with_arguments(
            command="config-test", service=self.service, arguments=config
        )

    def config_write(self, filename: str) -> dict:
        """Write the current configuration to a file on disk

        Args:
            filename:       Name of the configuration file

        Kea API Reference:
            https://kea.readthedocs.io/en/kea-2.2.0/api.html#config-write
        """
        return self.api.send_command_with_arguments(
            command="config-write",
            service=self.service,
            arguments={"filename": filename},
        )

    def list_commands(self) -> dict:
        """List all commands supported by the server/service

        Kea API Reference:
            https://kea.readthedocs.io/en/kea-2.2.0/api.html#ref-list-commands
        """
        return self.api.send_command_with_arguments(
            command="list-commands", service=self.service, arguments={}
        )

    def shutdown(self) -> dict:
        """Instructs the server daemon to initiate its shutdown procedure

        Kea API Reference:
            https://kea.readthedocs.io/en/kea-2.2.0/api.html#ref-shutdown
        """
        return self.api.send_command_with_arguments(
            command="shutdown", service=self.service, arguments={"exit-value": 123}
        )

    def status_get(self) -> dict:
        """Returns servers runtime information

        Kea API Reference:
            https://kea.readthedocs.io/en/kea-2.2.0/api.html#ref-status-get
        """
        return self.api.send_command(command="status-get", service=self.service)

    def version_get(self) -> dict:
        """Returns extended information about the Kea Version that is running

        Kea API Reference:
            https://kea.readthedocs.io/en/kea-2.2.0/api.html#ref-version-get
        """
        return self.api.send_command(command="version-get", service=self.service)
