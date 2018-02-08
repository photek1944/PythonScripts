#! python3
# windowsfilter.py -- add the pipe " OR " character to the end of any string to create a filterstring for Windows Explorer

import pyperclip

var = pyperclip.paste()
var = var.replace('T-','')
var = var.split('\r\n')

if var[-1] == "":
    del var[-1]

for i in range(len(var)):
    var[i] = str('*') + var[i]
   
var = ' OR '.join(var)
var = var + ' -_'
pyperclip.copy(var)

print('Creating Windows Search Filter: ' + var)
