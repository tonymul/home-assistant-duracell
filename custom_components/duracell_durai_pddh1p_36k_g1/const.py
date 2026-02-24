DOMAIN = "duracell_inverter"
DEFAULT_SCAN_INTERVAL = 2

SENSORS = [
    # ── BATTERY ──────────────────────────────────────────────────────
    {
        "name": "Duracell Battery SOC",
        "address": 8192, "unit_of_measurement": "%",
        "data_type": "uint16", "device_class": "battery", "state_class": "measurement",
    },
    {
        "name": "Duracell Battery Voltage",
        "address": 8198, "unit_of_measurement": "V", "scale": 0.1,
        "data_type": "uint16", "device_class": "voltage", "state_class": "measurement",
    },
    {
        "name": "Duracell Battery Current",
        "address": 8200, "unit_of_measurement": "A", "scale": 0.01,
        "data_type": "int16", "device_class": "current", "state_class": "measurement",
    },
    {
        "name": "Duracell Battery Power",
        "address": 8202, "unit_of_measurement": "W", "scale": 0.1,
        "data_type": "int16", "device_class": "power", "state_class": "measurement",
    },
    {
        "name": "Duracell Battery Temperature",
        "address": 8219, "unit_of_measurement": "°C",
        "data_type": "uint16", "device_class": "temperature", "state_class": "measurement",
    },
    {
        "name": "Duracell Battery Cell Voltage Max",
        "address": 8215, "unit_of_measurement": "mV",
        "data_type": "uint16", "device_class": "voltage", "state_class": "measurement",
    },
    {
        "name": "Duracell Battery Cell Voltage Min",
        "address": 8217, "unit_of_measurement": "mV",
        "data_type": "uint16", "device_class": "voltage", "state_class": "measurement",
    },
    {
        "name": "Duracell Battery Cell Temp Max",
        "address": 8220, "unit_of_measurement": "°C",
        "data_type": "uint16", "device_class": "temperature", "state_class": "measurement",
    },
    {
        "name": "Duracell Battery Cell Temp Min",
        "address": 8222, "unit_of_measurement": "°C",
        "data_type": "uint16", "device_class": "temperature", "state_class": "measurement",
    },
    {
        "name": "Duracell Battery Capacity",
        "address": 8238, "unit_of_measurement": "Ah", "scale": 0.1,
        "data_type": "uint16", "state_class": "measurement",
    },
    {
        "name": "Duracell Battery Max Charge Current",
        "address": 8240, "unit_of_measurement": "A", "scale": 0.1,
        "data_type": "uint16", "device_class": "current", "state_class": "measurement",
    },
    {
        "name": "Duracell Battery Max Discharge Current",
        "address": 8241, "unit_of_measurement": "A", "scale": 0.1,
        "data_type": "uint16", "device_class": "current", "state_class": "measurement",
    },
    {
        "name": "Duracell BMS Status Word",
        "address": 8210, "unit_of_measurement": None,
        "data_type": "uint16", "state_class": "measurement",
    },
    {
        "name": "Duracell BMS Fault Code",
        "address": 8211, "unit_of_measurement": None,
        "data_type": "uint16", "state_class": "measurement",
    },

    # ── INVERTER ─────────────────────────────────────────────────────
    {
        "name": "Duracell Inverter Temperature",
        "address": 4124, "unit_of_measurement": "°C",
        "data_type": "uint16", "device_class": "temperature", "state_class": "measurement",
    },
    {
        "name": "Duracell Inverter Operating Mode",
        "address": 4202, "unit_of_measurement": None,
        "data_type": "uint16", "state_class": "measurement",
    },
    {
        "name": "Duracell Inverter Status Word",
        "address": 4187, "unit_of_measurement": None,
        "data_type": "uint16", "state_class": "measurement",
    },
    {
        "name": "Duracell Inverter Rated Power",
        "address": 4195, "unit_of_measurement": "W",
        "data_type": "uint16", "device_class": "power", "state_class": "measurement",
    },
    {
        "name": "Duracell AC Output Voltage",
        "address": 4176, "unit_of_measurement": "V", "scale": 0.1,
        "data_type": "uint16", "device_class": "voltage", "state_class": "measurement",
    },
    {
        "name": "Duracell AC Output Power",
        "address": 4106, "unit_of_measurement": "W", "scale": 0.1,
        "data_type": "uint16", "device_class": "power", "state_class": "measurement",
    },
    {
        "name": "Duracell AC Output Current",
        "address": 4180, "unit_of_measurement": "A", "scale": 0.01,
        "data_type": "uint16", "device_class": "current", "state_class": "measurement",
    },
    {
        "name": "Duracell Output Frequency",
        "address": 4920, "unit_of_measurement": "Hz", "scale": 0.01,
        "data_type": "uint16", "device_class": "frequency", "state_class": "measurement",
    },

    # ── GRID ─────────────────────────────────────────────────────────
    {
        "name": "Duracell Grid Voltage",
        "address": 4097, "unit_of_measurement": "V", "scale": 0.1,
        "data_type": "uint16", "device_class": "voltage", "state_class": "measurement",
    },
    {
        "name": "Duracell Grid Frequency",
        "address": 4101, "unit_of_measurement": "Hz", "scale": 0.01,
        "data_type": "uint16", "device_class": "frequency", "state_class": "measurement",
    },
    {
        "name": "Duracell Grid Power",
        "address": 2041, "unit_of_measurement": "W", "scale": 0.01,
        "data_type": "int16", "device_class": "power", "state_class": "measurement",
    },
    {
        "name": "Duracell Grid CT Current",
        "address": 4894, "unit_of_measurement": "A", "scale": 0.01,
        "data_type": "int16", "device_class": "current", "state_class": "measurement",
    },

    # ── SOLAR / PV ───────────────────────────────────────────────────
    {
        "name": "Duracell PV Power Total",
        "address": 4100, "unit_of_measurement": "W", "scale": 0.1,
        "data_type": "uint16", "device_class": "power", "state_class": "measurement",
    },
    {
        "name": "Duracell MPPT1 Voltage",
        "address": 4112, "unit_of_measurement": "V", "scale": 0.1,
        "data_type": "uint16", "device_class": "voltage", "state_class": "measurement",
    },
    {
        "name": "Duracell MPPT1 Current",
        "address": 4113, "unit_of_measurement": "A", "scale": 0.01,
        "data_type": "uint16", "device_class": "current", "state_class": "measurement",
    },
    {
        "name": "Duracell MPPT1 Power",
        "address": 4115, "unit_of_measurement": "W", "scale": 0.1,
        "data_type": "uint16", "device_class": "power", "state_class": "measurement",
    },

    # ── LOAD ─────────────────────────────────────────────────────────
    {
        "name": "Duracell Load Power",
        "address": 2046, "unit_of_measurement": "W", "scale": 0.01,
        "data_type": "int16", "device_class": "power", "state_class": "measurement",
    },

    # ── ENERGY STATISTICS ────────────────────────────────────────────
    {
        "name": "Duracell PV Energy Total",
        "address": 4130, "unit_of_measurement": "kWh",
        "data_type": "uint16", "device_class": "energy", "state_class": "total_increasing",
    },
    {
        "name": "Duracell PV Energy Today",
        "address": 4136, "unit_of_measurement": "kWh", "scale": 0.001,
        "data_type": "uint16", "device_class": "energy", "state_class": "total_increasing",
    },
    {
        "name": "Duracell PV Energy This Month",
        "address": 4132, "unit_of_measurement": "kWh", "scale": 0.1,
        "data_type": "uint16", "device_class": "energy", "state_class": "total_increasing",
    },
    {
        "name": "Duracell PV Peak Power Today",
        "address": 4156, "unit_of_measurement": "W", "scale": 0.1,
        "data_type": "uint16", "device_class": "power", "state_class": "measurement",
    },

    # ── CONFIGURATION ────────────────────────────────────────────────
    {
        "name": "Duracell Grid Charge Max Power",
        "address": 8470, "unit_of_measurement": "W",
        "data_type": "uint16", "device_class": "power", "state_class": "measurement",
    },
    {
        "name": "Duracell Max Charge Power",
        "address": 8472, "unit_of_measurement": "W",
        "data_type": "uint16", "device_class": "power", "state_class": "measurement",
    },
    {
        "name": "Duracell Max Discharge Power",
        "address": 8474, "unit_of_measurement": "W",
        "data_type": "uint16", "device_class": "power", "state_class": "measurement",
    },
    {
        "name": "Duracell Charge End SOC",
        "address": 8473, "unit_of_measurement": "%",
        "data_type": "uint16", "device_class": "battery", "state_class": "measurement",
    },
    {
        "name": "Duracell Discharge End SOC",
        "address": 8475, "unit_of_measurement": "%",
        "data_type": "uint16", "device_class": "battery", "state_class": "measurement",
    },
    {
        "name": "Duracell Discharge End SOC On-Grid",
        "address": 8522, "unit_of_measurement": "%",
        "data_type": "uint16", "device_class": "battery", "state_class": "measurement",
    },
    {
        "name": "Duracell Force Charge SOC Start",
        "address": 8516, "unit_of_measurement": "%",
        "data_type": "uint16", "device_class": "battery", "state_class": "measurement",
    },
    {
        "name": "Duracell Force Charge SOC Stop",
        "address": 8517, "unit_of_measurement": "%",
        "data_type": "uint16", "device_class": "battery", "state_class": "measurement",
    },
    {
        "name": "Duracell Max Grid Input",
        "address": 8485, "unit_of_measurement": "W",
        "data_type": "uint16", "device_class": "power", "state_class": "measurement",
    },
    {
        "name": "Duracell Max Grid Force Charge",
        "address": 8528, "unit_of_measurement": "W",
        "data_type": "uint16", "device_class": "power", "state_class": "measurement",
    },
]
