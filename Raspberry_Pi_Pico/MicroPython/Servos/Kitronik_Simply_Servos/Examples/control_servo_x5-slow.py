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
        if current_switch2_state == 1:  # Switch 2 is on (connected to 3V3)
            target_position2 = target_hi2
        else:  # Switch 2 is off (connected to GND through pull-down)
            target_position2 = target_lo2
        
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
        
    # If switch 3 state has changed
    if current_switch3_state != previous_switch3_state:
        if current_switch3_state == 1:  # Switch 3 is on (connected to 3V3)
            target_position3 = target_hi3
        else:  # Switch 3 is off (connected to GND through pull-down)
            target_position3 = target_lo3
        
        # Move servo 3 to target position slowly
        if current_servo3_position < target_position3:
            for position in range(current_servo3_position, target_position3 + 1):
                board.goToPosition(3, position)
                sleep(delay)
        elif current_servo3_position > target_position3:
            for position in range(current_servo3_position, target_position3 - 1, -1):
                board.goToPosition(3, position)
                sleep(delay)
        
        # Update current servo 3 position and previous switch 3 state
        current_servo3_position = target_position3
        previous_switch3_state = current_switch3_state
        
    # If switch 4 state has changed
    if current_switch4_state != previous_switch4_state:
        if current_switch4_state == 1:  # Switch 4 is on (connected to 3V3)
            target_position4 = target_hi4
        else:  # Switch 4 is off (connected to GND through pull-down)
            target_position4 = target_lo4
        
        # Move servo 4 to target position slowly
        if current_servo4_position < target_position4:
            for position in range(current_servo4_position, target_position4 + 1):
                board.goToPosition(4, position)
                sleep(delay)
        elif current_servo4_position > target_position4:
            for position in range(current_servo4_position, target_position4 - 1, -1):
                board.goToPosition(4, position)
                sleep(delay)
        
        # Update current servo 4 position and previous switch 4 state
        current_servo4_position = target_position4
        previous_switch4_state = current_switch4_state

    # If switch 5 state has changed
    if current_switch5_state != previous_switch5_state:
        if current_switch5_state == 1:  # Switch 5 is on (connected to 3V3)
            target_position5 = target_hi5
        else:  # Switch 5 is off (connected to GND through pull-down)
            target_position5 = target_lo5
        
        # Move servo 5 to target position slowly
        if current_servo5_position < target_position5:
            for position in range(current_servo5_position, target_position5 + 1):
                board.goToPosition(5, position)
                sleep(delay)
        elif current_servo5_position > target_position5:
            for position in range(current_servo5_position, target_position5 - 1, -1):
                board.goToPosition(5, position)
                sleep(delay)
        
        # Update current servo 5 position and previous switch 5 state
        current_servo5_position = target_position5
        previous_switch5_state = current_switch5_state
    
    # Wait a bit before checking again
    sleep(0.1)
