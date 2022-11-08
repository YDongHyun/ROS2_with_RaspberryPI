import time
from sshkeyboard import listen_keyboard
from gpiozero import Motor

motor_r=Motor(forward=12,backward=16)
motor_l=Motor(forward=20,backward=21)

def press(key):
    if key=="w":
        motor_r.forward(speed=0.5)
        motor_l.forward(speed=0.5)
    elif key=="a":
        motor_r.forward(speed=0.5)
        motor_l.backward(speed=0.5)
    elif key=="s":
        motor_r.backward(speed=0.5)
        motor_l.backward(speed=0.5)
    elif key=="d":
        motor_r.backward(speed=0.5)
        motor_l.forward(speed=0.5)
    elif key=="space":
        motor_r.forward(speed=0)
        motor_l.backward(speed=0)

listen_keyboard(on_press=press)

