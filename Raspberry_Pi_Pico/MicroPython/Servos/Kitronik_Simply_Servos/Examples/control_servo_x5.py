from machine import Pin
from time import sleep

# Initialise the PIO and set them to drive the servo pins
# In the "SimplyServos.py" module change the value for the initial angle - 500 for 0 degrees to 2500 for 180 degrees

import SimplyServos
board = SimplyServos.KitronikSimplyServos()

# Set up switch pins as input with pull-down resistor
switch1 = Pin(0, Pin.IN, Pin.PULL_DOWN)
switch2 = Pin(1, Pin.IN, Pin.PULL_DOWN)
switch3 = Pin(26, Pin.IN, Pin.PULL_DOWN)
switch4 = Pin(27, Pin.IN, Pin.PULL_DOWN)
switch5 = Pin(28, Pin.IN, Pin.PULL_DOWN)

# Previous switch states
previous_switch1_state = switch1.value()
previous_switch2_state = switch2.value()
previous_switch3_state = switch3.value()
previous_switch4_state = switch4.value()
previous_switch5_state = switch5.value()

while True:
    # Read current switch states
    current_switch1_state = switch1.value()
    current_switch2_state = switch2.value()
    current_switch3_state = switch3.value()
    current_switch4_state = switch4.value()
    current_switch5_state = switch5.value()
    
    # If switch 1 state has changed
    if current_switch1_state != previous_switch1_state:
        if current_switch1_state == 1:  # Switch 1 is on (connected to VCC)
            board.goToPosition(1, 45)  # Move servo 1 to 45 degrees
        else:  # Switch 1 is off (connected to GND through pull-down)
            board.goToPosition(1, 135)   # Move servo 1 to 135 degrees
        # Update previous switch state
        previous_switch1_state = current_switch1_state
    
    # If switch 2 state has changed
    if current_switch2_state != previous_switch2_state:
        if current_switch2_state == 1:  # Switch 2 is on (connected to VCC)
            board.goToPosition(2, 30)  # Move servo 2 to 30 degrees
        else:  # Switch 2 is off (connected to GND through pull-down)
            board.goToPosition(2, 150)   # Move servo 2 to 150 degrees
        # Update previous switch state
        previous_switch2_state = current_switch2_state
        
    # If switch 3 state has changed
    if current_switch3_state != previous_switch3_state:
        if current_switch3_state == 1:  # Switch 3 is on (connected to VCC)
            board.goToPosition(3, 30)  # Move servo 3 to 30 degrees
        else:  # Switch 3 is off (connected to GND through pull-down)
            board.goToPosition(3, 150)   # Move servo 3 to 150 degrees
        # Update previous switch state
        previous_switch3_state = current_switch3_state
        
    # If switch 4 state has changed
    if current_switch4_state != previous_switch4_state:
        if current_switch4_state == 1:  # Switch 4 is on (connected to VCC)
            board.goToPosition(4, 30)  # Move servo 4 to 30 degrees
        else:  # Switch 4 is off (connected to GND through pull-down)
            board.goToPosition(4, 150)   # Move servo 4 to 150 degrees
        # Update previous switch state
        previous_switch4_state = current_switch4_state
        
    # If switch 5 state has changed
    if current_switch5_state != previous_switch5_state:
        if current_switch5_state == 1:  # Switch 5 is on (connected to VCC)
            board.goToPosition(5, 30)  # Move servo 5 to 30 degrees
        else:  # Switch 5 is off (connected to GND through pull-down)
            board.goToPosition(5, 150)   # Move servo 5 to 150 degrees
        # Update previous switch state
        previous_switch5_state = current_switch5_state        
        
    # Wait a bit before checking again
    sleep(0.1)
    