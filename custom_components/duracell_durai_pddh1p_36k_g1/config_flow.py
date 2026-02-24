import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResult
from pymodbus.client import ModbusTcpClient
from .const import DOMAIN, DEFAULT_SCAN_INTERVAL

STEP_USER_DATA_SCHEMA = vol.Schema(
    {
        vol.Required("host"): str,
        vol.Optional("port", default=502): int,
        vol.Optional("scan_interval", default=DEFAULT_SCAN_INTERVAL): int,
    }
)


def _test_connection(host: str, port: int) -> bool:
    """Try to connect and read a register to verify the inverter is reachable."""
    try:
        client = ModbusTcpClient(host, port=port)
        if not client.connect():
            return False
        result = client.read_holding_registers(4101, count=1, device_id=1)
        client.close()
        return not result.isError()
    except Exception:
        return False


class DuracellConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle the config flow for Duracell Dura-i Inverter."""

    VERSION = 1

    async def async_step_user(self, user_input=None) -> FlowResult:
        errors = {}

        if user_input is not None:
            host = user_input["host"]
            port = user_input["port"]

            # Check for duplicate entry
            await self.async_set_unique_id(f"{host}:{port}")
            self._abort_if_unique_id_configured()

            # Test connection in executor
            ok = await self.hass.async_add_executor_job(
                _test_connection, host, port
            )
            if not ok:
                errors["base"] = "cannot_connect"
            else:
                return self.async_create_entry(
                    title=f"Duracell Inverter ({host})",
                    data=user_input,
                )

        return self.async_show_form(
            step_id="user",
            data_schema=STEP_USER_DATA_SCHEMA,
            errors=errors,
        )
