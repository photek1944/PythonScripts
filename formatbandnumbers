#! python3
# formatbandnumbers.py

import re, pyperclip

print("Vul de landcode in en druk op 'Enter'")
landcode = input()

string = pyperclip.paste()
ro1 = re.compile(r'(\d+)/((\d{2})(\d{2})?)')
string = ro1.sub(landcode + r'\2-\1', string)

ro2 = re.compile(r'([a-zA-Z]{2})(\d{2})(\d{2})(-\d+)')
string = ro2.sub(r'\1\3\4', string)

ro3 = re.compile(r'[a-zA-Z]{2}\d{2}-\d+')
listBandnumbers = ro3.findall(string)

listBandnumbers = ('\r\n'.join(listBandnumbers))

pyperclip.copy(listBandnumbers)

print(listBandnumbers)
