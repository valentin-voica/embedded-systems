# Import required libraries
from machine import Pin, I2C
import bme280

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000) # Initialize the I2C method
bme = bme280.BME280(i2c=i2c) # Create the BME280 object

print(bme.values) # print raw data

# Temperature reading and conversion
tempString = bme.values[0]
tempString = tempString.replace("C", "")
tempFloat = float(tempString)
temp = round(tempFloat, 1)

# Atmospheric pressure reading and conversion
hpaString = bme.values[1]
hpaString = hpaString.replace("hPa","")
hpaFloat = float(hpaString)
mmhg = round((float(hpaString)*0.75006), 1)

# Humidity reading and conversion
humString = bme.values[2]
humString = humString.replace("%", "")
humFloat = float(humString)
hum = round(humFloat, 1)

# Send the values to console
print("Temperature:", temp, "°C")
print("Atmospheric pressure:", mmhg, "mmHg")
print("Humidity:", hum, "%")
