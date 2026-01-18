# Import required libraries
from machine import Pin
from time import sleep
import network

led = Pin("LED", Pin.OUT)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
# Disable power-saving mode when wireless chip is idle
wlan.config(pm = 0xa11140)
ssid = 'SSID'
passkey = 'PASSKEY'
wlan.connect(ssid, passkey)

# Wait 10 seconds to connect
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    sleep(1)

# Handle connection status
if wlan.status() != 3:
    raise RuntimeError('Cannot connect to Wi-Fi.') # network connectivity fails
else:
    # Blink LED...
    s = 5
    while s > 0:
        s -= 1
        led.value(1)
        sleep(0.2)
        led.value(0)
        sleep(0.2)
        led.value(1)
        
    # ... then print connection information
    status = wlan.ifconfig()
    print( 'Connected to ' + ssid + '. ' + 'My IP: ' + status[0] )
