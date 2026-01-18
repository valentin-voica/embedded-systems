from machine import Pin
from time import sleep

# Initialise the PIO and set them to drive the servo pins
# In the "SimplyServos.py" module change the value for the initial angle - 500 for 0 degrees to 2500 for 180 degrees

import SimplyServos
board = SimplyServos.KitronikSimplyServos()

# Set up switch pin as input with pull-down resistor
switch1 = Pin(0, Pin.IN, Pin.PULL_DOWN)
switch2 = Pin(1, Pin.IN, Pin.PULL_DOWN)
switch3 = Pin(26, Pin.IN, Pin.PULL_DOWN)
switch4 = Pin(27, Pin.IN, Pin.PULL_DOWN)
switch5 = Pin(28, Pin.IN, Pin.PULL_DOWN)

# Previous switch state
previous_switch1_state = switch1.value()
previous_switch2_state = switch2.value()
previous_switch3_state = switch3.value()
previous_switch4_state = switch4.value()
previous_switch5_state = switch5.value()

# Current servo position (same as defined in SimplyServos.py module)
current_servo1_position = 90
current_servo2_position = 90
current_servo3_position = 90
current_servo4_position = 90
current_servo5_position = 90

# Slow movement delay
delay = 0.01  # Smaller value => faster movement; set to 0 for no delay

# Define target positions in degrees with values between 0 and 180
target_lo1 = 0  # Min angle for servo 1
target_hi1 = 180  # Max angle for servo 1
target_lo2 = 0  # Min angle for servo 2
target_hi2 = 180  # Max angle for servo 2
target_lo3 = 0  # Min angle for servo 3
target_hi3 = 180  # Max angle for servo 3
target_lo4 = 0  # Min angle for servo 4
target_hi4 = 180  # Max angle for servo 4
target_lo5 = 0  # Min angle for servo 5
target_hi5 = 180  # Max angle for servo 5

while True:
    # Read current switch states
    current_switch1_state = switch1.value()
    current_switch2_state = switch2.value()
    current_switch3_state = switch3.value()
    current_switch4_state = switch4.value()
    current_switch5_state = switch5.value()
    
    # If switch 1 state has changed
    if current_switch1_state != previous_switch1_state:
        if current_switch1_state == 1:  # Switch 1 is on (connected to 3V3)
            target_position1 = target_hi1
        else:  # Switch 1 is off (connected to GND through pull-down)
            target_position1 = target_lo1
        
        # Move servo 1 to target position slowly
        if current_servo_position < target_position:
            for position in range(current_servo_position, target_position + 1):
                board.goToPosition(1, position)
                sleep(delay)
        elif current_servo_position > target_position:
            for position in range(current_servo_position, target_position - 1, -1):
                board.goToPosition(1, position)
                sleep(delay)
        
        # Update current servo position and previous switch state
        current_servo_position = target_position
        previous_switch_state = current_switch_state
    
    # Wait a bit before checking again
    sleep(0.1)
