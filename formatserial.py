#! python3
# formatserial.py

#formats band numbers to PIPA format

import re, pyperclip

string = pyperclip.paste()

print("Vul de landcode in en druk op 'Enter'")
print("Voorbeeld: 'BE'")
landcode = input()

print("Vul het jaartal in en druk op 'Enter'")
print("Voorbeeld: '17'")
jaartal = input()

print("Vul het serienummer in en druk op 'Enter'")
print("Voorbeeld: '4250'")
serienummer = input()

#/123
ro3 = re.compile(r'/(\d{3})')
string = ro3.sub(landcode + jaartal + '-' + serienummer + r'\1', string)

#1234567-17 & 1234567-2017
ro1 = re.compile(r'(\d{7})-((\d{2})(\d{2})?)')
string = ro1.sub(landcode + r'\2-\1', string)

#17-1234567
ro2 = re.compile(r'(\d{2})(-\d{7})')
string = ro2.sub(landcode + r'\1\2', string)

#XX17-1234567 - adds formatted band numbers to list of strings regardless of countrycode
roX = re.compile(r'[a-zA-Z]{2}\d{2}-\d+')
listBandnumbers = roX.findall(string)

listBandnumbers = ('\r\n'.join(listBandnumbers))

pyperclip.copy(listBandnumbers)

print(listBandnumbers)
