import keyboard
from turtle import *

title('WhiteBoard')
speed(0)
bgcolor('darkgray')

while True:
    if keyboard.is_pressed('Esc'):
        bye()
        break

    if keyboard.is_pressed('w'):
        setheading(90)
        forward(3)

    if keyboard.is_pressed('d'):
        setheading(0)
        forward(3)

    if keyboard.is_pressed('s'):
        setheading(-90)
        forward(3)

    if keyboard.is_pressed('a'):
        setheading(180)
        forward(3)

    if keyboard.is_pressed('0'):
        color('black')
    
    if keyboard.is_pressed('1'):
        color('red')

    if keyboard.is_pressed('2'):
        color('orange')

    if keyboard.is_pressed('3'):
        color('yellow')

    if keyboard.is_pressed('4'):
        color('green')

    if keyboard.is_pressed('5'):
        color('blue')

    if keyboard.is_pressed('6'):
        color('purple')

    if keyboard.is_pressed('c'):
        clear()

    if keyboard.is_pressed('q'):
        penup()

    if keyboard.is_pressed('e'):
        pendown()

    if keyboard.is_pressed('r'):
        penup()
        goto(0, 0)
        pendown()
