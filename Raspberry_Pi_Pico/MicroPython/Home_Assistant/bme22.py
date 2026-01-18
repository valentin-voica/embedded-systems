# Import required libraries
from machine import Pin, I2C
from time import sleep
import network
import socket
import bme280
import json

led = Pin("LED", Pin.OUT) # Pin setup
i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000) # Initialize the I2C method
bme = bme280.BME280(i2c=i2c) # Create the BME280 object

# Network configuration
#######################
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.config(pm = 0xa11140) # Disable power-saving mode when wireless chip is idle
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
    raise RuntimeError('Cannot connect to Wi-Fi')
else:
    # Blink LED...
    s = 5
    while s > 0:
        s -= 1
        led.value(1)
        sleep(0.2)
        led.value(0)
        sleep(0.2)
    # ... then print connection information
    status = wlan.ifconfig()
    print('Connected to ' + ssid + '. ' + 'My IP: ' + status[0])
# Open a socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)
print('Listening on', addr)

# Home Assistant Integration
############################
while True:
    if wlan.status() == 3:
        led.value(1)
    else:
        led.value(0)
        print("Disconnected from the network.")
    try:
        cl, addr = s.accept()
        print('client connected from', addr)
        request = cl.recv(1024)
        request = str(request)
        print(request)
        # Temperature reading and conversion
        tempString = bme.values[0]
        tempString = tempString.replace("C", "")
        tempFloat = float(tempString)
        temp = round(tempFloat, 1)
        # Atmospheric pressure reading and conevrsion
        hpaString = bme.values[1]
        hpaString = hpaString.replace("hPa","")
        hpaFloat = float(hpaString)
        mmhg = round((float(hpaString)*0.75006), 1)
        # Humidity reading and conversion
        humString = bme.values[2]
        humString = humString.replace("%", "")
        humFloat = float(humString)
        hum = round(humFloat, 1)
        # Preparing and sending data to Home Assistant
        data = { "temperature": temp, "atmosphericPressure": mmhg, "humidity": hum }
        JsonData = json.dumps(data)
        cl.send('HTTP/1.0 200 OK\r\nContent-type: application/json\r\n\r\n') # Send headers notifying the receiver that the data is of type Json for application consumption
        cl.send(JsonData) # Send the Json data
        cl.close() # Close the connection
    except KeyboardInterrupt:
        break