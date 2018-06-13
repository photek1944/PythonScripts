#! python3

#navBatchkiller.py

import pyperclip, pyautogui, time, os

os.chdir(r'C:\Users\NielsC\AppData\Local\Programs\Python\Python35\Scripts')

from win32api import GetKeyState
from win32con import VK_CAPITAL

# store band numbers in list
bandNrs = pyperclip.paste()
bandNrs = bandNrs.split('\r\n')
del bandNrs[-1]

# create filter
var = pyperclip.paste()
var = var.split('\r\n')

if var[-1] == "":
    del var[-1]
    
var = '|'.join(var)
pyperclip.copy(var)

print('Creating Navision filter: ' + var)

print('Welk financieel document wil je toevoegen?')
finDoc = input()

print('Kopieer het bereik met ringnummers.' +
      '\nKlik op de bovenste record van de duiventabel in Navision.' +
      '\nNa 5 seconden begint het doden van duiven.')

time.sleep(5)

pyautogui.PAUSE = 0.01

if GetKeyState(VK_CAPITAL) == 1:
    pyautogui.press('capslock')
    
for i in range(len(bandNrs)):
    pyautogui.press('enter')
    time.sleep(2)   
    pyautogui.hotkey('ctrl','shift','e')
    pyautogui.PAUSE = 2
    for x in range(0,5):
        pyautogui.press('\t')
    pyautogui.typewrite('Dood')
    finDoc2Location = pyautogui.locateOnScreen('finDoc2.JPG')
    mouseCoordinates = pyautogui.center(finDoc2Location)
    pyautogui.moveTo(mouseCoordinates)
    pyautogui.moveRel(100, 0, duration = 0.25)
    pyautogui.click()
##    for x in range(0,41):
##        pyautogui.press('\t')
    pyautogui.hotkey('ctrl','c')
    findoc2 = pyperclip.paste()
    if findoc2 != "":
        pyautogui.press('\t')
        pyautogui.press('\t')
    pyautogui.keyDown('ctrlleft'); pyautogui.press('enter')
    pyautogui.keyUp('ctrlleft')
    time.sleep(2)
    print(bandNrs[i] + ' kreeg de status "dood" en financieel document ' + finDoc + '.')
