import RPi.GPIO as GPIO
rled = 16
yled = 20
gled = 21
rswitch = 5
yswitch = 6
gswitch = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(rled, GPIO.OUT)
GPIO.setup(yled, GPIO.OUT)
GPIO.setup(gled, GPIO.OUT)
GPIO.setup(rswitch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(yswitch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(gswitch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        val1 =GPIO.input(rswitch)
        print(val1)
        GPIO.output(rled, val1)
        val2 = GPIO.input(yswitch)
        print(val2)
        GPIO.output(yled, val2)
        val3 = GPIO.input(gswitch)
        print(val3)
        GPIO.output(gled, val3)
finally:
    GPIO.cleanup()
    print('cleanup and exit')