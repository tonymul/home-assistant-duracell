import voluptuous as vol
from homeassistant import config_entries
from .const import DOMAIN, DEFAULT_SCAN_INTERVAL

class DuracellInverterConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="Duracell Hybrid Inverter", data=user_input)

        data_schema = vol.Schema({
            vol.Required("host"): str,
            vol.Optional("port", default=502): int,
            vol.Optional("scan_interval", default=DEFAULT_SCAN_INTERVAL): int,
        })
        return self.async_show_form(step_id="user", data_schema=data_schema)