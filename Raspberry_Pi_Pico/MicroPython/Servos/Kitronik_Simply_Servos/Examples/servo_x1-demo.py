from machine import Pin
from time import sleep

# Initialise the PIO and set them to drive the servo pins
# In the "SimplyServos.py" module change the value for the initial angle - 500 for 0 degrees to 2500 for 180 degrees

import SimplyServos
board = SimplyServos.KitronikSimplyServos()

# Set up switch pin as input with pull-down resistor
switch = Pin(0, Pin.IN, Pin.PULL_DOWN)

# Previous switch state
previous_switch_state = switch.value()

# Define target positions in degrees with values between 0 and 180
target_lo = 30 # Min angle
target_hi = 150  # Max angle

while True:
    # Read current switch state
    current_switch_state = switch.value()
    
    # If switch state has changed
    if current_switch_state != previous_switch_state:
        if current_switch_state == 1:  # Switch is on (connected to 3V3)
            board.goToPosition(1, target_hi)
        else:  # Switch is off (connected to GND through pull-down)
            board.goToPosition(1, target_lo)
        # Update previous switch state
        previous_switch_state = current_switch_state
    
    # Wait a bit before checking again
    sleep(0.1)
