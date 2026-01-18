from machine import Pin
from time import ticks_ms,sleep_ms

led_onboard = Pin("LED", Pin.OUT)
button = Pin(0, Pin.IN, Pin.PULL_DOWN)

def wait_pin_change(pin):
    # wait for pin to change value
    # it needs to be stable for a continuous 20ms
    cur_value = pin.value()
    active = 0
    while active < 20:
        if pin.value() != cur_value:
            active += 1
        else:
            active = 0
        sleep_ms(10)

while True:
    wait_pin_change(button)
    led_onboard.toggle()
