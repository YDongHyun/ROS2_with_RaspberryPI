import keyboard
 
while True:
    key=keyboard.read_key()
    if key=="q":
        print("press")
        break
    else:
        if key:
            print(key)
            key=False
