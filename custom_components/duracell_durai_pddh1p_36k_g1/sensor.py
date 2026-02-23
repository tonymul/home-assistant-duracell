from pymodbus.client.sync import ModbusTcpClient
from homeassistant.components.sensor import SensorEntity
from .const import SENSORS

async def async_setup_entry(hass, entry, async_add_entities):
    host = entry.data["host"]
    port = entry.data.get("port", 502)

    client = ModbusTcpClient(host, port=port)
    entities = [DuracellSensor(client, s) for s in SENSORS]

    async_add_entities(entities, update_before_add=True)

class DuracellSensor(SensorEntity):
    def __init__(self, client, sensor_info):
        self._client = client
        self._name = sensor_info["name"]
        self._address = sensor_info["address"]
        self._unit = sensor_info.get("unit")
        self._scale = sensor_info.get("scale", 1)
        self._data_type = sensor_info.get("data_type", "uint16")
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
        result = self._client.read_holding_registers(self._address, 1)
        if result.isError():
            self._state = None
            return
        value = result.registers[0]
        if self._data_type == "int16" and value > 32767:
            value -= 65536
        self._state = value * self._scale