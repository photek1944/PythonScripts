#! python3
# copyfilenames.py

import pyperclip, os, re

currentDir = pyperclip.paste()      
filenameList = os.listdir(currentDir)
ro = re.compile(r'(.*?)(_[a-zA-Z0-9]*)?(\..*)+')
for i in range(len(filenameList)):
    filenameList[i] = ro.sub(r'\1', filenameList[i])
filenameList = '\r\n'.join(filenameList)
pyperclip.copy(filenameList)

print('Copying filenames without extention' + str(filenameList))
