import RPi.GPIO as GPIO
import time

BUZZER_PIN = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 1)
pwm.start(10)

melody = [262, 294, 330, 349, 392, 440, 494]
a = [4,4,5,5,4,4,2,2,4,4,2,2,1,1,4,4,5,5,4,4,2,2,4,2,1,2,0,0]
for i in a:
        pwm.ChangeFrequency(melody[i])
        time.sleep(0.5)
pwm.stop()
GPIO.cleanup()