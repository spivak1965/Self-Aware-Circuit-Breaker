# Self-Aware Circuit Breaker

**Description:**  
An Arduino-based predictive circuit breaker that monitors current and voltage to protect a load from spikes. The system can be simulated in Python or run on actual hardware.  

---

## Overview
This project implements a **self-aware circuit breaker** that predicts current spikes and disconnects the load before damage occurs.  

- **Python simulation:** Gradually generates current and voltage spikes, predicts them in advance, and sends ON/OFF commands to the Arduino. Real-time plots show the system’s operation.  
- **Arduino hardware:** Receives commands from Python (or directly from sensors in a real hardware setup) to control a Solid State Relay (SSR) that switches the load.  

⚡ The predictive logic works the same way whether the spike is **simulated in Python** or occurs **in real hardware**.  

**Key Features:**
- Predicts current spikes before they occur
- Automatically disconnects load via SSR
- Real-time monitoring and plotting of current, voltage, and load state
- Python simulation for safe testing and visualization

---

## Components

**Hardware:**
- Arduino Uno
- ACS712 30A Current Sensor
- Voltage Sensor Module
- ZGT-25DA Solid State Relay (SSR)
- AC Load (e.g., lamp)
- Wires, breadboard, connectors

**Software:**
- Arduino IDE
- Python 3.x
- Python libraries: `pyserial`, `matplotlib`

---

## Hardware Setup

1. **ACS712 Current Sensor**
   - VCC → Arduino 5V  
   - GND → Arduino GND  
   - OUT → Arduino A0  

2. **Voltage Sensor Module**
   - VCC → Arduino 5V  
   - GND → Arduino GND  
   - OUT → Arduino A1  

3. **SSR (ZGT-25DA)**
   - Control side: + → Arduino D8, – → GND  
   - Load side: AC mains → Lamp  

4. Place photos in `hardware/photos_of_setup/` and include the **circuit diagram** in `hardware/circuit_diagram.png`.  

> ⚠️ **Safety Warning:** Be careful when working with AC mains voltage. Use insulated wires and avoid touching live circuits.  

---

## Software Setup

1. **Arduino Code**
   - Upload `jn6_arduino.ino` to the Arduino Uno.
   - This code receives `"ON"` or `"OFF"` commands via serial and switches the SSR accordingly.

2. **Python Simulation**
   - Run `software/python/spike_monitor.py` to simulate and visualize predictive spikes.
   - The script sends `"ON"`/`"OFF"` commands to the Arduino based on predicted spikes.
   - Real-time plots display current, voltage, and load state, with OFF periods highlighted in red.

> ✅ The simulation demonstrates the predictive spike logic safely. The **same logic works identically on real hardware** when actual spikes occur.  

---

## Operation Flow

High-level operation of the circuit:

