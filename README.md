# Duracell Hybrid Inverter HACS Integration

This is a **Home Assistant HACS integration** for the Duracell Hybrid Inverter (Dura-i series). It exposes all available **live data, statistics, and configuration registers** via sensors and supports **GUI setup** through Home Assistant.

---

## Features

* Full support for 40+ sensors:

  * Battery SOC, voltage, current, power, temperature
  * Inverter temperature
  * Grid voltage, frequency, power, CT current
  * PV power and MPPT sensors
  * Daily/total energy statistics
  * Configuration registers (charge/discharge limits, SOC, max power)
* Automatic sensor creation
* Configurable **scan interval**
* GUI setup for IP and port (no YAML required)
* HACS-ready installation

---

## Installation

1. Clone or download the repository to your local machine.
2. Compress the folder `custom_components/duracell_inverter/` into `duracell_inverter.zip`.
3. In Home Assistant, go to **HACS → Integrations → + → Custom Repository → Upload ZIP**.
4. Install the integration.

---

## Setup

1. Go to **Configuration → Integrations → Add Integration → Duracell Hybrid Inverter**.
2. Enter your inverter **IP address**, **port**, and optionally the **scan interval** (default 2 seconds).
3. Click **Submit**.
4. All sensors will automatically be created and updated.

---

## Requirements

* Home Assistant Core
* Python library: `pymodbus>=2.5.3`

---

## Support

* Documentation: [https://github.com/tonymul/home-assistant-duracell](https://github.com/tonymul/home-assistant-duracell)
* Issue Tracker: [https://github.com/tonymul/home-assistant-duracell/issues](https://github.com/tonymul/home-assistant-duracell/issues)

---

## License

MIT License
