from machine import Pin
from time import sleep

# Initialise the PIO and set them to drive the servo pins
# In the "SimplyServos.py" module change the value for the initial angle - 500 for 0 degrees to 2500 for 180 degrees

import SimplyServosTOU
board = SimplyServosTOU.KitronikSimplyServos()

# Set up switch pin as input with pull-up resistor
switch1 = Pin(0, Pin.IN, Pin.PULL_UP)  # This switch controls TOU 1
switch2 = Pin(1, Pin.IN, Pin.PULL_UP)  # This switch controls TOU 2

# Previous switch state
previous_switch1_state = switch1.value()
previous_switch2_state = switch2.value()

# Current servo position (same as defined in SimplyServos.py module)
current_servo1_position = 90
current_servo2_position = 90

# Slow movement delay
delay = 0.01  # Smaller value => faster movement; set to 0 for no delay

# Define servos' target angle (between 0 and 180 degrees)
target_lo1 = 88  # Min angle for servo 1 (TOU 1)
target_hi1 = 92  # Max angle for servo 1 (TOU 1)
target_lo2 = 88  # Min angle for servo 2 (TOU 2)
target_hi2 = 92  # Max angle for servo 2 (TOU 2)

while True:
    # Read current switch states
    current_switch1_state = switch1.value()
    current_switch2_state = switch2.value()
    
    # If switch 1 state has changed
    if current_switch1_state != previous_switch1_state:
        if current_switch1_state == 0:  # Switch 1 is off (connected to GND)
            target_position1 = target_lo1
        else:  # Switch 1 is on (connected to 3V3 through pull-up)
            target_position1 = target_hi1
        
        # Move servo 1 to target position slowly
        if current_servo1_position < target_position1:
            for position in range(current_servo1_position, target_position1 + 1):
                board.goToPosition(1, position)
                sleep(delay)
        elif current_servo1_position > target_position1:
            for position in range(current_servo1_position, target_position1 - 1, -1):
                board.goToPosition(1, position)
                sleep(delay)
        
        # Update current servo 1 position and previous switch 1 state
        current_servo1_position = target_position1
        previous_switch1_state = current_switch1_state
        
    # If switch 2 state has changed
    if current_switch2_state != previous_switch2_state:
        if current_switch2_state == 0:  # Switch 2 is on (connected to GND)
            target_position2 = target_lo2
        else:  # Switch 2 is on (connected to 3V3 through pull-up)
            target_position2 = target_hi2
        
        # Move servo 2 to target position slowly
        if current_servo2_position < target_position2:
            for position in range(current_servo2_position, target_position2 + 1):
                board.goToPosition(2, position)
                sleep(delay)
        elif current_servo2_position > target_position2:
            for position in range(current_servo2_position, target_position2 - 1, -1):
                board.goToPosition(2, position)
                sleep(delay)
        
        # Update current servo 2 position and previous switch 2 state
        current_servo2_position = target_position2
        previous_switch2_state = current_switch2_state
        
    # Wait a bit before checking again
    sleep(0.1)
