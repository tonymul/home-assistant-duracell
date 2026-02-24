import logging
from datetime import timedelta
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from pymodbus.client import ModbusTcpClient
from .const import DOMAIN, SENSORS, DEFAULT_SCAN_INTERVAL
from .sensor import fetch_modbus_data

_LOGGER = logging.getLogger(__name__)
PLATFORMS = ["sensor"]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Duracell from a config entry."""
    host = entry.data["host"]
    port = entry.data.get("port", 502)
    scan_interval = entry.data.get("scan_interval", DEFAULT_SCAN_INTERVAL)

    client = ModbusTcpClient(host, port=port)

    coordinator = DataUpdateCoordinator(
        hass,
        _LOGGER,
        name="duracell",
        update_method=lambda: hass.async_add_executor_job(fetch_modbus_data, client),
        update_interval=timedelta(seconds=scan_interval),
    )

    try:
        await coordinator.async_config_entry_first_refresh()
    except Exception as err:
        raise ConfigEntryNotReady(
            f"Unable to connect to Duracell inverter at {host}:{port}"
        ) from err

    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = coordinator

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)
    return unload_ok
