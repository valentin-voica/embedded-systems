from machine import Pin
import time
import dht 

dSensor1 = dht.DHT11(Pin(0))
dSensor2 = dht.DHT22(Pin(2))

def readDHT():
    try:
        dSensor1.measure()
        dSensor2.measure()
        temp1 = dSensor1.temperature()
        temp2 = dSensor2.temperature()
        hum1 = dSensor1.humidity()
        hum2 = dSensor2.humidity()
        print('Reading from the DHT11 sensor')
        print('-----------------------------')
        print('Temperature: {} °C'.format(temp1))
        print('Humidity: {} % '.format(hum1))
        print('+++++++++++++++++++++++++++++')
        print('Reading from the DHT22 sensor')
        print('-----------------------------')
        print('Temperature: {} °C'.format(temp2))
        print('Humidity: {} % '.format(hum2))
        print('=============================')
        print()
    except OSError as e:
        print('Failed to read data from DHT sensors')
    
while True:
    readDHT()
    time.sleep(5)