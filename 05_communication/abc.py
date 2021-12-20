from lcd import drivers
import time
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
PIN = 4

display = drivers.Lcd()

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, PIN)
        if humidity is not None and temperature is not None:
            import datetime
            now = datetime.datetime.now()
            display.lcd_display_string(now.strftime("%x%X"),1)
            display.lcd_display_string(f"{temperature: .1f}C,{humidity: .1f}%",2)
        else:
            print("Read error")
    
finally:
    display.lcd_clear()