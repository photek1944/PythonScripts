#! python3
# navcopypaste.py

import pyperclip, pyautogui, time

from win32api import GetKeyState
from win32con import VK_CAPITAL

var = pyperclip.paste()
var = var.split('\r\n')

print('Selecteer de bovenste cel van een kolom in Navision. Na 3 seconden begint het plakken')
time.sleep(3)

pyautogui.PAUSE = 0.01

if GetKeyState(VK_CAPITAL) == 1:
    pyautogui.press('capslock')

for i in var:
    print('Pasting: ' + i)
    pyautogui.typewrite(i)
    pyautogui.press('down')
