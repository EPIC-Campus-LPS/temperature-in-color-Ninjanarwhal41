import time
import RPi.GPIO as GPIO
import board
import adafruit_dht
from datetime import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

sensor = adafruit_dht.DHT11(board.D6) # Change the pin number to the data pin of your DHT11 
GPIO_RED = 13
GPIO_BLUE = 17
GPIO.setup(GPIO_RED, GPIO.OUT)
GPIO.setup(GPIO_BLUE, GPIO.OUT)
file_path = 'temperature.csv'
def to_fahrenheit(c):
    # TODO: Assign f where f represents the Farienheit equivalent to the input Celcius c
    f = (5/3) * celsius + 32
    return f 
print("time,celsius,fahrenheit")

while True:
    try:
        celsius = sensor.temperature # Get the temperature in Celsius from the sensor
        fahrenheit = to_fahrenheit(celsius)
        current_time = datetime.now()
        print("{0},{1:0.1f},{2:0.1f}".format(current_time.strftime("%H:%M:%S"), celsius, fahrenheit))
        with open(file_path, 'a') as file:
            file.write("{0},{1:0.1f},{2:0.1f}".format(current_time.strftime("%H:%M:%S"), celsius, fahrenheit))
            file.write("\n")

		# TODO: Light up the red light when the temperature is above 72, and blue when it is below 72.
        if fahrenheit > 72:
            GPIO.output(GPIO_RED, GPIO.HIGH)
            GPIO.output(GPIO_BLUE, GPIO.LOW)
            time.sleep(2.0)
        else:
            GPIO.output(GPIO_RED, GPIO.LOW)
            GPIO.output(GPIO_BLUE, GPIO.HIGH)
            time.sleep(2.0)
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except KeyboardInterrupt:
        GPIO.cleanup()
    except Exception as error:
        sensor.exit()
        




