import RPi.GPIO as GPIO

LED_PIN = 22

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)



@app.route("/")
def hello():
    return '''
    <p>Hello, Flask!</p>
    <a href="/LED/ON">LED ON</a>
    <a href="/LED/OFF">LED OFF</a>
    '''

@app.route("/LED/<op>")
def led_op(op):
    if op == "ON":
        GPIO.output(LED_PIN, GPIO.HIGH)
        return'''
            <p>LED ON</p>
            <a href="/">Go home</a>
        '''
    elif op == "OFF":
        return'''
             <p>LEF OFF</p>
            <a href="/">Go home</a>
        '''

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()
