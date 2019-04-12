import time
import random
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(12, GPIO.IN)

print("Reaction time game \n \n")

GPIO.output(3, GPIO.HIGH)
GPIO.output(13, GPIO.HIGH)
time.sleep(2)
GPIO.output(3, GPIO.LOW)
GPIO.output(13, GPIO.LOW)

print("we will start in 5 sec")
time.sleep(5)

GPIO.output(3, GPIO.HIGH)

r = random.randint(1, 10)
time.sleep(r)
GPIO.output(3, GPIO.LOW)
GPIO.output(13, GPIO.HIGH)

start = time.time()