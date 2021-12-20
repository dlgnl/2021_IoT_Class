import RPi.GPIO as GPIO
ys=6
y=20
r=16
rs=5
g=21
gs=13
GPIO.setmode(GPIO.BCM)
GPIO.setup(r, GPIO.OUT)
GPIO.setup(y, GPIO.OUT)
GPIO.setup(g, GPIO.OUT)
GPIO.setup(ys, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(rs, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(gs, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
try:
    while True:
        GPIO.output(r, GPIO.input(rs))
        GPIO.output(y, GPIO.input(ys))
        GPIO.output(g, GPIO.input(gs))
finally:
    GPIO.cleanup()
    print('cleanup and exit')