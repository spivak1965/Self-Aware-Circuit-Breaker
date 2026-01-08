import matplotlib.pyplot as plt
import serial
import time

# ------------------- Arduino Setup -------------------
arduino = serial.Serial('COM3', 9600)  # replace with your Arduino COM port
time.sleep(2)  # wait for Arduino reset

# ------------------- Simulation Parameters -------------------
dt = 0.2
total_time = 35
current_base = 0.26
voltage_base = 2.2
current_spike = 0.29
voltage_spike = 0.4
prediction_advance = 1.0  # seconds before spike
spikes = [(5, 12), (20, 27)]  # start/end times of spikes

# ------------------- Data Storage -------------------
time_data = []
current_data = []
voltage_data = []
light_data = []

# ------------------- Plot Setup -------------------
fig, ax = plt.subplots()
line_current, = ax.plot([], [], label="Current (A)", color="blue", linewidth=2)
line_voltage, = ax.plot([], [], label="Voltage (V)", color="orange", linewidth=2)
line_light, = ax.plot([], [], label="Light ON(1)/OFF(0)", color="green", linewidth=4)
ax.set_xlabel("Time (s)")
ax.set_ylabel("Values")
ax.set_xlim(0, total_time)
ax.set_ylim(0, 3)
ax.legend()

time_sim = 0

# ------------------- Simulation Loop -------------------
while time_sim <= total_time:
    # --- Gradual current & voltage spikes ---
    current = current_base
    voltage = voltage_base
    for start, end in spikes:
        if start <= time_sim <= end:
            factor = (time_sim - start) / (end - start)
            current += current_spike * factor
            voltage += voltage_spike * factor
            break

    # --- Predictive spike logic ---
    predicted_spike = False
    for start, end in spikes:
        start_predict = max(0, start - prediction_advance)
        if start_predict <= time_sim <= end:
            predicted_spike = True
            break

    # --- Light state ---
    light_on = not predicted_spike

    # --- Send command to Arduino ---
    if light_on:
        arduino.write(b'ON\n')
    else:
        arduino.write(b'OFF\n')

    # --- Store data ---
    time_data.append(time_sim)
    current_data.append(current)
    voltage_data.append(voltage)
    light_data.append(1 if light_on else 0)

    # --- Remove previous red rectangles safely ---
    for coll in ax.collections:
        coll.remove()

    # --- Draw OFF periods as red rectangles ---
    i = 0
    while i < len(light_data):
        if light_data[i] == 0:
            start_idx = i
            while i < len(light_data) and light_data[i] == 0:
                i += 1
            end_idx = i
            ax.fill_between(time_data[start_idx:end_idx], 0, 3, color='red', alpha=0.3)
        else:
            i += 1

    # --- Update graph lines ---
    line_current.set_data(time_data, current_data)
    line_voltage.set_data(time_data, voltage_data)
    line_light.set_data(time_data, light_data)

    ax.relim()
    ax.autoscale_view()
    plt.pause(dt)
    time_sim += dt

plt.show()
