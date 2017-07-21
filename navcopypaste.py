#! python3
# navcopypaste.py

import pyperclip, pyautogui, time

var = pyperclip.paste()
var = var.split('\r\n')

print('Selecteer de bovenste cel van een kolom in Navision. Na 5 seconden begint het plakken')
time.sleep(5)

pyautogui.PAUSE = 0.05

for i in var:
    print('Pasting: ' + i)
    pyautogui.typewrite(i)
    pyautogui.press('down')
