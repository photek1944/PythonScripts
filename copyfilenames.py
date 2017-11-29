#! python3
# copyfilenames.py | copies file names from any directory on clipboard and turns it into a sorted unique set

import pyperclip, os, re

currentDir = pyperclip.paste()      
filenameList = os.listdir(currentDir)
if filenameList[-1] == 'Thumbs.db':
    del filenameList[-1]
ro = re.compile(r'(.*?)(_[a-zA-Z0-9]*)?(\..*)+')
for i in range(len(filenameList)):
    filenameList[i] = ro.sub(r'\1', filenameList[i])
filenameList = list(set(filenameList))
filenameList.sort()
filenameList = '\r\n'.join(filenameList)
pyperclip.copy(filenameList)

print('Copying filenames without extention' + str(filenameList))
