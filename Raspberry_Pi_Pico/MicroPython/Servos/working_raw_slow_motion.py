from machine import Pin, PWM
import time

# Define the servo pin
servo_pin = 2
# Define the switch pin
switch_pin = 0

# Create a PWM object for the servo
pwm = PWM(Pin(servo_pin, Pin.OUT), freq=50)

# Function to set the servo angle
def set_servo_angle(angle):
    # Map angle to pulse width in microseconds
    pulse_width = int(((angle / 180) * 1000) + 1000)
    pulse_width = max(1000, min(pulse_width, 2000))
    # Set the duty cycle based on the pulse width
    pwm.duty_u16(int((pulse_width / 20000) * 65535))

# Function to move servo slowly to a target angle
def move_servo_slowly(target_angle, current_angle, step_size=1, delay=0.03):
    if target_angle > current_angle:
        for angle in range(current_angle, target_angle + 1, step_size):
            set_servo_angle(angle)
            time.sleep(delay)
    elif target_angle < current_angle:
        for angle in range(current_angle, target_angle - 1, -step_size):
            set_servo_angle(angle)
            time.sleep(delay)

# Set up switch pin as input with pull-down resistor
switch = Pin(switch_pin, Pin.IN, Pin.PULL_DOWN)

# Initial servo angle
current_angle = 180
set_servo_angle(current_angle)

while True:
    # Read current switch state
    current_switch_state = switch.value()
    
    # If switch state has changed
    if current_switch_state == 1:  # Switch is on (connected to VCC)
        target_angle = 135
    else:  # Switch is off (connected to GND through pull-down)
        target_angle = 180
    
    # Move servo slowly to target angle
    move_servo_slowly(target_angle, current_angle)
    current_angle = target_angle
    
    # Wait a bit before checking again
    time.sleep(0.1)
