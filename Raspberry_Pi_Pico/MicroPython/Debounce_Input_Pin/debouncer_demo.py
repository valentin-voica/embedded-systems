from machine import Pin
from debouncer import Debouncer

debouncer = Debouncer(Pin(0, Pin.IN, Pin.PULL_DOWN))
led_onboard = Pin("LED", Pin.OUT)

while True:
    state = debouncer()
    led_onboard(state)