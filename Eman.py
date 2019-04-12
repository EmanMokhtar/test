import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)

for i in range (0, 200):
    # Turn on the leds one by one

    GPIO.output(7, GPIO.HIGH)        #white led
    time.sleep(1)

    GPIO.output(5, GPIO.HIGH)       # yellow
    time.sleep(1)

    GPIO.output(3, GPIO.HIGH)       # blue
    time.sleep(1)

    # turn off the leds one by one
    GPIO.output(7, GPIO.LOW)
    time.sleep(1)

    GPIO.output(5, GPIO.LOW)
    time.sleep(1)

    GPIO.output(3, GPIO.LOW)
    time.sleep(1)

    #at the end of the iteration the blue one will blink twice
    GPIO.output(3, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(3, GPIO.LOW)
    GPIO.output(3, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(3, GPIO.LOW)


GPIO.cleanup()