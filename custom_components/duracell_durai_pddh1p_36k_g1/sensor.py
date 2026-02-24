import logging
from pymodbus.client import ModbusTcpClient
from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from .const import DOMAIN, SENSORS

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback):
    """Set up Duracell sensors from a config entry."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    entities = [DuracellSensor(coordinator, s) for s in SENSORS]
    async_add_entities(entities, update_before_add=True)


def fetch_modbus_data(client):
    """Fetch all sensor data from the Modbus device."""
    data = {}
    if not client.connect():
        _LOGGER.error("Failed to connect to Modbus device")
        return {s["name"]: None for s in SENSORS}

    try:
        for s in SENSORS:
            address = s["address"]
            data_type = s.get("data_type", "uint16")
            scale = s.get("scale", 1)
            try:
                result = client.read_holding_registers(address, count=1, device_id=1)
                if result.isError():
                    data[s["name"]] = None
                    continue
                value = result.registers[0]
                if data_type == "int16" and value > 32767:
                    value -= 65536
                data[s["name"]] = value * scale
            except Exception:
                _LOGGER.exception("Error reading register for %s", s["name"])
                data[s["name"]] = None
    finally:
        client.close()

    return data


class DuracellSensor(SensorEntity):
    """Representation of a single Duracell sensor."""

    def __init__(self, coordinator, sensor_info):
        self.coordinator = coordinator
        self._sensor_info = sensor_info
        self._name = sensor_info["name"]
        self._unit = sensor_info.get("unit_of_measurement")
        self._device_class = sensor_info.get("device_class")
        self._state_class = sensor_info.get("state_class")

    @property
    def unique_id(self):
        return f"duracell_{self._sensor_info['address']}"

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self.coordinator.data.get(self._name) if self.coordinator.data else None

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def device_class(self):
        return self._device_class

    @property
    def state_class(self):
        return self._state_class

    @property
    def should_poll(self):
        return False

    async def async_update(self):
        pass