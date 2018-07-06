#! python3
# createFolders.py | uses filenames from a range on the clipboard to create folders for each filename in a given directory
# Created on: 06/07/2018

import pyperclip, os

print('Kopieer het bereik met bestandsnamen voor de folders die je wil aanmaken en typ OK + enterknop')
var = input()

filenameList = pyperclip.paste()
filenameList = filenameList.split('\r\n')
if filenameList[-1] == "":
    del filenameList[-1]
filenameList = list(set(filenameList))
filenameList.sort()

print(filenameList)

print('Kopieer het pad waar de mappen gemaakt moeten worden en typ OK + enterknop')
var = input()
currentDir = pyperclip.paste()

foldernameList = os.listdir(currentDir)
print('foldernameList: ' + str(foldernameList))

#remove folders already created in currentDir to avoid duplicate error
filenameList = list(set(filenameList) - set(foldernameList))

#create folders
for i in filenameList:
    os.makedirs(currentDir + '\\' + i)
    print('Map aangemaakt: ' + currentDir + '\\' + i)
