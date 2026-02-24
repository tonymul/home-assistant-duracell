import logging
from pymodbus.client import ModbusTcpClient
from homeassistant.components.sensor import SensorEntity, SensorDeviceClass, SensorStateClass
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN, SENSORS

_LOGGER = logging.getLogger(__name__)

OPERATING_MODE_MAP = {
    0: "Standby",
    1: "No Grid",
    2: "Fault",
    3: "Updating",
    4: "PV Charging",
    5: "AC Charging",
    6: "Discharging",
    7: "PV + AC Charging",
    8: "PV + AC + Bypass",
    9: "PV + Bypass",
    10: "Bypass",
    11: "PV + Bypass",
    17: "Grid-Tied Normal",
}

BMS_FAULT_MAP = {
    0: "No Fault",
    1: "Cell Overvoltage",
    2: "Cell Undervoltage",
    3: "Pack Overvoltage",
    4: "Pack Undervoltage",
    5: "Charge Overtemp",
    6: "Charge Undertemp",
    7: "Discharge Overtemp",
    8: "Discharge Undertemp",
    9: "Charge Overcurrent",
    10: "Discharge Overcurrent",
    11: "Short Circuit",
    12: "BMS IC Fault",
    13: "Software Fault",
}

BATTERY_CAPACITY_WH = 5120


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Duracell sensors from a config entry."""
    coordinator = hass.data[DOMAIN][entry.entry_id]

    entities: list[SensorEntity] = []

    # Add all Modbus sensors
    for sensor_info in SENSORS:
        entities.append(DuracellModbusSensor(coordinator, sensor_info))

    # Add calculated sensors
    entities.extend([
        DuracellInverterModeTextSensor(coordinator),
        DuracellBMSFaultTextSensor(coordinator),
        DuracellBatteryStatusSensor(coordinator),
        DuracellCellVoltageSpreadSensor(coordinator),
        DuracellBatteryTimeRemainingSensor(coordinator),
        DuracellSelfConsumptionSensor(coordinator),
        DuracellSolarCoverageSensor(coordinator),
    ])

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


def _device_info() -> DeviceInfo:
    return DeviceInfo(
        identifiers={(DOMAIN, "2445-28030366ph")},
        name="Duracell Dura-i Inverter",
        manufacturer="Duracell Energy",
        model="DURA5",
        serial_number="2445-28030366ph",
    )


class DuracellModbusSensor(CoordinatorEntity, SensorEntity):
    """A sensor that reads a single Modbus register."""

    def __init__(self, coordinator, sensor_info):
        super().__init__(coordinator)
        self._sensor_info = sensor_info
        self._attr_name = sensor_info["name"]
        self._attr_unique_id = f"duracell_{sensor_info['address']}"
        self._attr_native_unit_of_measurement = sensor_info.get("unit_of_measurement")
        self._attr_device_class = sensor_info.get("device_class")
        self._attr_state_class = sensor_info.get("state_class")
        self._attr_device_info = _device_info()

    @property
    def native_value(self):
        if self.coordinator.data is None:
            return None
        return self.coordinator.data.get(self._sensor_info["name"])


class DuracellCalculatedSensor(CoordinatorEntity, SensorEntity):
    """Base class for sensors calculated from other sensor values."""

    def __init__(self, coordinator, name, unique_id):
        super().__init__(coordinator)
        self._attr_name = name
        self._attr_unique_id = unique_id
        self._attr_device_info = _device_info()

    def _get(self, sensor_name, fallback=None):
        """Safely retrieve a value from coordinator data."""
        if self.coordinator.data is None:
            return fallback
        val = self.coordinator.data.get(sensor_name)
        return val if val is not None else fallback


class DuracellInverterModeTextSensor(DuracellCalculatedSensor):
    """Human-readable inverter operating mode."""

    def __init__(self, coordinator):
        super().__init__(coordinator, "Duracell Inverter Mode", "duracell_inverter_mode_text")
        self._attr_icon = "mdi:solar-power"

    @property
    def native_value(self):
        mode = self._get("Duracell Inverter Operating Mode")
        if mode is None:
            return None
        return OPERATING_MODE_MAP.get(int(mode), f"Unknown ({int(mode)})")


class DuracellBMSFaultTextSensor(DuracellCalculatedSensor):
    """Human-readable BMS fault description."""

    def __init__(self, coordinator):
        super().__init__(coordinator, "Duracell BMS Fault", "duracell_bms_fault_text")
        self._attr_icon = "mdi:alert-circle"

    @property
    def native_value(self):
        code = self._get("Duracell BMS Fault Code")
        if code is None:
            return None
        return BMS_FAULT_MAP.get(int(code), f"Unknown ({int(code)})")


class DuracellBatteryStatusSensor(DuracellCalculatedSensor):
    """Charging / Discharging / Idle status based on battery current."""

    def __init__(self, coordinator):
        super().__init__(coordinator, "Duracell Battery Status", "duracell_battery_status")

    @property
    def native_value(self):
        current = self._get("Duracell Battery Current", 0)
        if current > 0.5:
            return "Charging"
        elif current < -0.5:
            return "Discharging"
        return "Idle"

    @property
    def icon(self):
        val = self.native_value
        if val == "Charging":
            return "mdi:battery-charging"
        elif val == "Discharging":
            return "mdi:battery-minus"
        return "mdi:battery"


class DuracellCellVoltageSpreadSensor(DuracellCalculatedSensor):
    """Difference between max and min cell voltage — early imbalance warning."""

    def __init__(self, coordinator):
        super().__init__(coordinator, "Duracell Battery Cell Voltage Spread", "duracell_cell_voltage_spread")
        self._attr_native_unit_of_measurement = "mV"
        self._attr_device_class = SensorDeviceClass.VOLTAGE
        self._attr_state_class = SensorStateClass.MEASUREMENT
        self._attr_icon = "mdi:battery-alert"

    @property
    def native_value(self):
        vmax = self._get("Duracell Battery Cell Voltage Max")
        vmin = self._get("Duracell Battery Cell Voltage Min")
        if vmax is None or vmin is None:
            return None
        return round(vmax - vmin, 1)


class DuracellBatteryTimeRemainingSensor(DuracellCalculatedSensor):
    """Estimated minutes until full (charging) or empty (discharging)."""

    def __init__(self, coordinator):
        super().__init__(coordinator, "Duracell Battery Time Remaining", "duracell_battery_time_remaining")
        self._attr_native_unit_of_measurement = "min"
        self._attr_icon = "mdi:timer"
        self._attr_state_class = SensorStateClass.MEASUREMENT

    @property
    def native_value(self):
        soc = self._get("Duracell Battery SOC", 0)
        power = self._get("Duracell Battery Power", 0)
        if power is None or abs(power) < 10:
            return None
        if power > 0:
            # Charging — time to full
            remaining_wh = (1 - soc / 100) * BATTERY_CAPACITY_WH
            return round(remaining_wh / power * 60)
        else:
            # Discharging — time to empty
            remaining_wh = (soc / 100) * BATTERY_CAPACITY_WH
            return round(remaining_wh / abs(power) * 60)


class DuracellSelfConsumptionSensor(DuracellCalculatedSensor):
    """Percentage of PV generation being consumed on-site."""

    def __init__(self, coordinator):
        super().__init__(coordinator, "Duracell Self Consumption", "duracell_self_consumption")
        self._attr_native_unit_of_measurement = "%"
        self._attr_state_class = SensorStateClass.MEASUREMENT
        self._attr_icon = "mdi:home-lightning-bolt"

    @property
    def native_value(self):
        pv = self._get("Duracell PV Power Total", 0)
        load = self._get("Duracell Load Power", 0)
        if pv is None or pv < 10:
            return 0
        return round(min(max(load / pv * 100, 0), 100), 1)


class DuracellSolarCoverageSensor(DuracellCalculatedSensor):
    """Percentage of load being covered by solar."""

    def __init__(self, coordinator):
        super().__init__(coordinator, "Duracell Solar Coverage", "duracell_solar_coverage")
        self._attr_native_unit_of_measurement = "%"
        self._attr_state_class = SensorStateClass.MEASUREMENT
        self._attr_icon = "mdi:solar-panel"

    @property
    def native_value(self):
        pv = self._get("Duracell PV Power Total", 0)
        load = self._get("Duracell Load Power", 0)
        if load is None or load < 10:
            return 100
        return round(min(max(pv / load * 100, 0), 100), 1)
