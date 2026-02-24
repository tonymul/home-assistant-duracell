# Duracell Dura-i Inverter — Home Assistant Integration

A custom Home Assistant integration for the **Duracell Dura-i hybrid solar inverter** using Modbus TCP.

## Features

- **40+ sensors** covering battery, inverter, grid, solar, load, and energy statistics
- **Calculated sensors** built into the integration — no template YAML required:
  - Inverter Mode (human-readable text)
  - BMS Fault (human-readable text)
  - Battery Status (Charging / Discharging / Idle)
  - Battery Cell Voltage Spread (imbalance early warning)
  - Battery Time Remaining (minutes to full or empty)
  - Self Consumption %
  - Solar Coverage %
- All sensors grouped under a single **device** in the HA device registry
- Configurable poll interval (default 2 seconds)
- Setup via the Home Assistant UI — no YAML required

## Requirements

- Home Assistant 2023.1 or later
- Duracell Dura-i inverter with Modbus TCP enabled
- Inverter reachable on your local network
- `pymodbus` 3.11.x (installed automatically)

## Installation

### HACS (Recommended)

1. Open HACS in Home Assistant
2. Go to **Integrations** → **Custom Repositories**
3. Add `https://github.com/YOUR_USERNAME/duracell_inverter` with category **Integration**
4. Search for **Duracell Dura-i Inverter** and install
5. Restart Home Assistant

### Manual

1. Copy the `custom_components/duracell_inverter` folder into your HA `config/custom_components/` directory
2. Restart Home Assistant

## Setup

1. Go to **Settings → Devices & Services → Add Integration**
2. Search for **Duracell Dura-i Inverter**
3. Enter your inverter's local IP address
4. Optionally adjust the Modbus port (default 502) and poll interval (default 2s)
5. Click **Submit**

## Enabling Modbus TCP on the Inverter

Log into the inverter web portal (browse to the inverter's IP address), go to **Settings → Communication** and enable **Modbus TCP**. The default port is 502.

## Sensors

### Battery
| Sensor | Unit | Notes |
|--------|------|-------|
| Battery SOC | % | State of charge |
| Battery Voltage | V | Pack voltage |
| Battery Current | A | Positive = charging |
| Battery Power | W | Positive = charging |
| Battery Temperature | °C | Pack temperature |
| Battery Cell Voltage Max | mV | Highest cell |
| Battery Cell Voltage Min | mV | Lowest cell |
| Battery Cell Voltage Spread | mV | Max − Min, imbalance indicator |
| Battery Cell Temp Max | °C | |
| Battery Cell Temp Min | °C | |
| Battery Capacity | Ah | BMS reported capacity |
| Battery Max Charge Current | A | BMS limit |
| Battery Max Discharge Current | A | BMS limit |
| Battery Status | — | Charging / Discharging / Idle |
| Battery Time Remaining | min | To full or empty |
| BMS Status Word | — | Raw bitmask |
| BMS Fault Code | — | Numeric fault code |
| BMS Fault | — | Human-readable fault description |

### Inverter
| Sensor | Unit | Notes |
|--------|------|-------|
| Inverter Temperature | °C | |
| Inverter Operating Mode | — | Numeric mode code |
| Inverter Mode | — | Human-readable mode |
| Inverter Rated Power | W | |
| Inverter Status Word | — | Raw bitmask |
| AC Output Voltage | V | |
| AC Output Power | W | |
| AC Output Current | A | |
| Output Frequency | Hz | |

### Grid
| Sensor | Unit | Notes |
|--------|------|-------|
| Grid Voltage | V | |
| Grid Frequency | Hz | |
| Grid Power | W | Positive = importing |
| Grid CT Current | A | |

### Solar / PV
| Sensor | Unit | Notes |
|--------|------|-------|
| PV Power Total | W | |
| MPPT1 Voltage | V | |
| MPPT1 Current | A | |
| MPPT1 Power | W | |
| Self Consumption | % | PV used on-site |
| Solar Coverage | % | Load covered by solar |

### Energy Statistics
| Sensor | Unit | Notes |
|--------|------|-------|
| PV Energy Total | kWh | Lifetime generation |
| PV Energy Today | kWh | |
| PV Energy This Month | kWh | |
| PV Peak Power Today | W | |

### Load
| Sensor | Unit | Notes |
|--------|------|-------|
| Load Power | W | Total house consumption |

### Configuration (read-only)
| Sensor | Unit |
|--------|------|
| Grid Charge Max Power | W |
| Max Charge Power | W |
| Max Discharge Power | W |
| Charge End SOC | % |
| Discharge End SOC | % |
| Discharge End SOC On-Grid | % |
| Force Charge SOC Start | % |
| Force Charge SOC Stop | % |
| Max Grid Input | W |
| Max Grid Force Charge | W |

## Tested Hardware

- Duracell DURA5 (5kW) with 5.12kWh LiFePO4 battery

## Contributing

Pull requests welcome. If you have a different Duracell inverter model and can share a Modbus register scan, please open an issue.

## License

MIT
