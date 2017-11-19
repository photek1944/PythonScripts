#! python3
# formatbandnumbers.py

#formats band numbers to PIPA format

import re, pyperclip

print("Vul de gewenste landcode in en druk op 'Enter'")
landcode = input()

string = pyperclip.paste()

#!band numbers with backslash

#1234567/17 & 1234567/2017
ro1 = re.compile(r'(\d{7})/((\d{2})(\d{2})?)')
string = ro1.sub(landcode + r'\2-\1', string)

#17/1234567
ro3 = re.compile(r'(\d{2})/(\d{7})')
string = ro3.sub(landcode + r'\1-\2', string)

#2017/1234567
#ro4 = re.compile(r'(\d{2})(\d{2})(-\d+)')
#string = ro4.sub(landcode + r'\2\3', string)

#XX2017/1234567
#ro2 = re.compile(r'([a-zA-Z]{2})(\d{2})(\d{2})(-\d{7})')
#string = ro2.sub(r'\1\3\4', string)

#!band numbers with dash

#1234567-17 & 1234567-2017
ro1 = re.compile(r'(\d{7})-((\d{2})(\d{2})?)')
string = ro1.sub(landcode + r'\2-\1', string)

#17-1234567
ro3 = re.compile(r'(\d{2})(-\d{7})')
string = ro3.sub(landcode + r'\1\2', string)

#XX17-1234567 - adds formatted band numbers to list of strings regardless of countrycode
roX = re.compile(r'[a-zA-Z]{2}\d{2}-\d+')
listBandnumbers = roX.findall(string)

#2017-1234567
#ro4 = re.compile(r'(\d{2})(\d{2})(-\d{7})')
#string = ro4.sub(landcode + r'\2\3', string)

#XX2017-1234567
#ro2 = re.compile(r'([a-zA-Z]{2})(\d{2})(\d{2})(-\d{7})')
#string = ro2.sub(r'\1\3\4', string)

listBandnumbers = ('\r\n'.join(listBandnumbers))

pyperclip.copy(listBandnumbers)

print(listBandnumbers)
