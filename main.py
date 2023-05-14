from machine import Pin
import utime

def get_pressed_key():
    key = None
    for x, row in enumerate(row_pins):
        row.value(1)
        for y, column in enumerate(column_pins):
            if column.value() == 1:
                key = matrix_keyboard[x][y]
                break
        row.value(0)
        if key is not None:
            break
    return key

def unlock(time):
    lock.value(1)
    utime.sleep(time)
    lock.value(0)


matrix_keyboard = [[1, 2, 3, "A"],
                   [4, 5, 6, "B"],
                   [7, 8, 9, "C"],
                   ["*", 0, "#", "D"]]

row_pin_nums = [3, 4, 5, 6]
column_pin_nums = [7, 8, 9, 10]

row_pins = [Pin(pin_num, Pin.OUT) for pin_num in row_pin_nums]
column_pins = [Pin(pin_num, Pin.IN, Pin.PULL_DOWN) for pin_num in column_pin_nums]

lock = Pin(15, Pin.OUT)

try:
    pin_code = open("pin.txt", "r").readline()
except OSError:
    f = open("pin.txt", "w")
    f.write("0000")
    f.close()
    pin_code = "0000"
    
user_input = ""

pressed = False
access = False

while 1:
    key = get_pressed_key()
    
    if key is not None and not pressed:
        pressed = True
        
        if isinstance(key, int) and len(user_input) < 4:
            user_input += str(key)
        
        else:
            if key == "#":
                if user_input == pin_code:
                    unlock(2)
            
            elif key == "A":
                if user_input == pin_code and not access:
                    access = True
                    unlock(0.05)

            elif key == "B" and access and len(user_input) == 4:
                f = open("pin.txt", "w")
                f.write(user_input)
                f.close()
                
                pin_code = user_input
                access = False
                unlock(0.05)
            
            elif key == "D":
                access = False
		unlock(0.05)
            
            user_input = ""

    if key is None and pressed:
        pressed = False
         
