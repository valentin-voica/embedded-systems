# Import required libraries
from machine import Pin
from time import sleep
import network
import socket
import dht
import json

# Pin setup
led = Pin("LED", Pin.OUT)
sensor = dht.DHT22(Pin(2))

# Create network connection

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
# Disable power-saving mode when wireless chip is idle
wlan.config(pm = 0xa11140)
# Connect to WLAN
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
    raise RuntimeError('network connection failed')
else:
    # Blink LED...
    s = 5
    while s > 0:
        s -= 1
        led.value(1)
        sleep(0.2)
        led.value(0)
        sleep(0.2)
    # ... and print connection information
    status = wlan.ifconfig()
    print( 'Connected to ' + ssid + '. ' + 'My IP: ' + status[0] )

sleep(5)

# Open a socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)

# Display your IP address
print('Listening on', addr)

while True:
    if wlan.status() == 3:
        led.value(1)
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        print("Temperature: {}°C   Humidity: {:.0f}% ".format(temp, hum))
        sleep(10)
    else:
        led.value(0)
