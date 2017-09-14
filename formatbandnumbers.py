#! python3
# formatbandnumbers.py

#looks for strings with digits/yyyy or digits/yy or AZyy/digits

import re, pyperclip

print("Vul de landcode in en druk op 'Enter'")
landcode = input()

#1234567/17 & 1234567/2017
string = pyperclip.paste()
ro1 = re.compile(r'(\d+)/((\d{2})(\d{2})?)')
string = ro1.sub(landcode + r'\2-\1', string)

#XX2017-1234567
ro2 = re.compile(r'([a-zA-Z]{2})(\d{2})(\d{2})(-\d+)')
string = ro2.sub(r'\1\3\4', string)

#17-1234567
ro3 = re.compile(r'(\d{2})(-\d+)')
string = ro3.sub(landcode + r'\1\2', string)

#2017-1234567
ro4 = re.compile(r'(\d{2})(\d{2})(-\d+)')
string = ro4.sub(landcode + r'\2\3', string)

#XX17-1234567
roX = re.compile(r'[a-zA-Z]{2}\d{2}-\d+')
listBandnumbers = roX.findall(string)

listBandnumbers = ('\r\n'.join(listBandnumbers))

pyperclip.copy(listBandnumbers)

print(listBandnumbers)
