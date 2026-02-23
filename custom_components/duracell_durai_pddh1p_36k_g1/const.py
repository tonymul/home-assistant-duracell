DOMAIN = "duracell_inverter"
DEFAULT_SCAN_INTERVAL = 2

# Full sensor list
SENSORS = [

    # LIVE DATA
    {"name": "Duracell Battery SOC", "address": 8192, "type": "holding", "data_type": "uint16", "unit": "%"},
    {"name": "Duracell BMS Code", "address": 8194, "type": "holding", "data_type": "uint16", "unit": ""},
    {"name": "Duracell Battery Voltage", "address": 8198, "type": "holding", "data_type": "uint16", "unit": "V", "scale": 0.1},
    {"name": "Duracell Battery Current", "address": 8200, "type": "holding", "data_type": "int16", "unit": "A", "scale": 0.01},
    {"name": "Duracell Battery Power", "address": 8202, "type": "holding", "data_type": "int16", "unit": "W", "scale": 0.1},
    {"name": "Duracell Battery Temperature", "address": 8219, "type": "holding", "data_type": "uint16", "unit": "°C"},
    {"name": "Duracell Inverter Temperature", "address": 4124, "type": "holding", "data_type": "uint16", "unit": "°C"},
    {"name": "Duracell Grid Voltage", "address": 4097, "type": "holding", "data_type": "uint16", "unit": "V", "scale": 0.1},
    {"name": "Duracell Grid Frequency", "address": 4101, "type": "holding", "data_type": "uint16", "unit": "Hz", "scale": 0.01},
    {"name": "Duracell PV Power Total", "address": 4100, "type": "holding", "data_type": "uint16", "unit": "W", "scale": 0.1},
    {"name": "Duracell MPPT1 Voltage", "address": 4112, "type": "holding", "data_type": "uint16", "unit": "V", "scale": 0.1},
    {"name": "Duracell MPPT1 Current", "address": 4113, "type": "holding", "data_type": "uint16", "unit": "A", "scale": 0.01},
    {"name": "Duracell MPPT1 Power", "address": 4115, "type": "holding", "data_type": "uint16", "unit": "W", "scale": 0.1},
    {"name": "Duracell Grid Power", "address": 2041, "type": "holding", "data_type": "int16", "unit": "W", "scale": 0.01},
    {"name": "Duracell Load Power", "address": 2046, "type": "holding", "data_type": "int16", "unit": "W", "scale": 0.01},
    {"name": "Duracell Grid/CT Current", "address": 4894, "type": "holding", "data_type": "int16", "unit": "A", "scale": 0.01},

    # STATISTICS
    {"name": "Duracell PV Peak Power", "address": 4156, "type": "holding", "data_type": "uint16", "unit": "W", "scale": 0.1},
    {"name": "Duracell Energy Total", "address": 4130, "type": "holding", "data_type": "uint16", "unit": "kWh"},
    {"name": "Duracell Energy Today", "address": 4136, "type": "holding", "data_type": "uint16", "unit": "kWh", "scale": 0.001},

    # CONFIGURATION
    {"name": "Duracell Grid Charge Max Power", "address": 8470, "type": "holding", "data_type": "uint16", "unit": "W"},
    {"name": "Duracell Max Charge Power", "address": 8472, "type": "holding", "data_type": "uint16", "unit": "W"},
    {"name": "Duracell Max Discharge Power", "address": 8474, "type": "holding", "data_type": "uint16", "unit": "W"},
    {"name": "Duracell Charge End SOC", "address": 8473, "type": "holding", "data_type": "uint16", "unit": "%"},
    {"name": "Duracell Discharge End SOC", "address": 8475, "type": "holding", "data_type": "uint16", "unit": "%"},
    {"name": "Duracell Discharge End SOC On-Grid", "address": 8522, "type": "holding", "data_type": "uint16", "unit": "%"},
    {"name": "Duracell Force Charge SOC Start", "address": 8516, "type": "holding", "data_type": "uint16", "unit": "%"},
    {"name": "Duracell Force Charge SOC Stop", "address": 8517, "type": "holding", "data_type": "uint16", "unit": "%"},
    {"name": "Duracell Max Grid Input", "address": 8485, "type": "holding", "data_type": "uint16", "unit": "W"},
    {"name": "Duracell Max Grid Force Charge", "address": 8528, "type": "holding", "data_type": "uint16", "unit": "W"}

]