from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.entity import Entity

DOMAIN = "duracell"

# Define your sensors
SENSOR_MAP = [
    # Battery
    {"name": "Duracell Battery SOC", "address": 8192, "unit": "%", "scale": 1, "signed": False},
    {"name": "Duracell Battery Voltage", "address": 8198, "unit": "V", "scale": 0.1, "signed": False},
    {"name": "Duracell Battery Current", "address": 8200, "unit": "A", "scale": 0.01, "signed": True},
    {"name": "Duracell Battery Power", "address": 8202, "unit": "W", "scale": 0.1, "signed": True},
    {"name": "Duracell Battery Temp", "address": 8219, "unit": "°C", "scale": 1, "signed": False},
    # Inverter
    {"name": "Duracell Inverter Temp", "address": 4124, "unit": "°C", "scale": 1, "signed": False},
    # Grid
    {"name": "Duracell Grid Voltage", "address": 4097, "unit": "V", "scale": 0.1, "signed": False},
    {"name": "Duracell Grid Frequency", "address": 4101, "unit": "Hz", "scale": 0.01, "signed": False},
    # PV
    {"name": "Duracell PV Power", "address": 4100, "unit": "W", "scale": 0.1, "signed": False},
]

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the Duracell sensors."""
    sensors = []
    for sensor in SENSOR_MAP:
        sensors.append(DuracellSensor(sensor))
    async_add_entities(sensors, True)

class DuracellSensor(SensorEntity):
    """Representation of a Duracell inverter sensor."""

    def __init__(self, sensor_info):
        self._name = sensor_info["name"]
        self._address = sensor_info["address"]
        self._unit = sensor_info["unit"]
        self._scale = sensor_info["scale"]
        self._signed = sensor_info["signed"]
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    async def async_update(self):
        """Fetch new state data from the inverter via Modbus TCP."""
        try:
            # Get the Modbus hub
            hub = self.hass.data[DOMAIN]
            result = await hub.read_holding_registers(self._address, 1, slave=1)
            value = result.registers[0]
            if self._signed and value > 32767:
                value -= 65536
            self._state = value * self._scale
        except Exception as e:
            self._state = None
            self.hass.logger.error(f"Duracell sensor {self._name} update failed: {e}")