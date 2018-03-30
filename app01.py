import RPi.GPIO as GPIO
from flask import Flask, render_template
app = Flask(__name__)

led = 0

def ledOn():
    pin = 21
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 1)
    global led
    led = 1

def ledOff():
    pin = 21
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)
    global led
    led = 0

@app.route("/")
def index():
    return render_template('index.html', led=led)

@app.route('/led_on')
def led_on():
    ledOn()
    print("led on")
    return render_template('index.html', led=led)

@app.route('/led_off')
def led_off():
    ledOff()
    print("led off")
    return render_template('index.html', led=led)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
