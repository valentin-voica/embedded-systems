from machine import Pin
from time import ticks_ms,sleep_ms

debounce_time = 50 # Define the debounce time in milliseconds
button = Pin(0, Pin.IN, Pin.PULL_DOWN)
led_onboard = Pin("LED", Pin.OUT)

# Initialize the last state and last change time
last_state = button.value()
last_change_time = ticks_ms()

while True:
    current_state = button.value() # Read the current state of the toggle switch
    if current_state != last_state: # Check if the state has changed
        current_time = ticks_ms() # Get the current time
        if current_time - last_change_time >= debounce_time: # Check if the debounce time has passed
            last_state = current_state # Update the last state and last change time
            last_change_time = current_time
            # Toggle the LED
            if last_state == 1:
                led_onboard.value(1)
            else:
                led_onboard.value(0)

    # Wait a short time before checking again
    sleep_ms(10)
        