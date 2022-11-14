import pyautogui as spam
import time

msg = input('Your msg>>>')
tries = input('Number of msg>>>')

i = 0

time.sleep(5)

while i < int(tries):

    spam.typewrite(msg)
    spam.press('Enter')

    i+=1
