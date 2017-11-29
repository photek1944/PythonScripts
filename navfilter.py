#! python3
# navfilter.py -- add the pipe "|" character to the end of any string to create a filterstring for Microsoft Navision

import pyperclip

var = pyperclip.paste()
var = var.split('\r\n')

if var[-1] == "":
    del var[-1]
    
var = '|'.join(var)
pyperclip.copy(var)

print('Creating Navision filter: ' + var)
