from gpiozero import Motor
import time

motor = Motor(forward=26,backward=27)

while True:
	motor.forward()
