import RPi.GPIO as GPIO
import time
import spidev

LED_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
spi = spidev.SpiDev()

spi.open(0, 0)

spi.max_speed_hz = 1000000


# 0~7까지 채널에서 SPI 데이터 읽기
def analog_read(channel):
  # [byte_1, byte_2, byte_3]
  # byte_1 : 1
  # byte_2 : channel(0) + 8 -> 0000 1000 << 4 -> 1000 0000
  # byte_3 : 0
  ret = spi.xfer2([1, (channel + 8) << 4, 0])
  adc_out = ((ret[1] & 3) << 8) + ret[2]
  return adc_out

try:
    while True:
        reading = analog_read(0)
        print("Reading=%d"% reading)
        time.sleep(0.5)
        if reading <= 60:
         GPIO.output(LED_PIN, GPIO.HIGH)
         print("led on")
        else: 
         GPIO.output(LED_PIN, GPIO.LOW)
         print("led off")
         
finally:
    spi.close()
