from gpiozero import Motor
import time
import keyboard


motor_r = Motor(forward=12,backward=16)
motor_l = Motor(forward=21,backward=22)

while True:
    if keyboard.read_key() == "w":
        motor_r.foward(speed=0.5)
        motor_l.foward(speed=0.5)
    elif keyboard.read_key() == "a":
        motor_r.foward(speed=0.5)
        motor_l.backward(speed=0.5)
    elif keyboard.read_key() == "s":
        motor_r.backward(speed=0.5)
        motor_l.backward(speed=0.5)
    elif keyboard.read_key() == "d":
        motor_r.backward(speed=0.5)
        motor_l.foward(speed=0.5)
    else:
        continue
