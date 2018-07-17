#! python3
# Gendika_DNA_Split.py | Creates separate JPGs from PDF file for Gendika DNA-certificates

import sys, os, pyperclip
from PIL import Image

currentDir = pyperclip.paste()
os.chdir(currentDir)
PDFnameList = os.listdir(currentDir)
print(PDFnameList)

for x in range(len(PDFnameList)):
    with open(PDFnameList[x],"rb") as file:
        file.seek(0)
        pdf = file.read()

    startmark = b"\xff\xd8"
    startfix = 0
    endmark = b"\xff\xd9"
    endfix = 2

    i = 0
    njpg = 0
  
    while True:
        istream = pdf.find(b"stream", i)
        if istream < 0:
            break
        istart = pdf.find(startmark, istream, istream + 20)
        if istart < 0:
            i = istream + 20
            continue
        iend = pdf.find(b"endstream", istart)
        if iend < 0:
            raise Exception("Didn't find end of stream!")
        iend = pdf.find(endmark, iend - 20)
        if iend < 0:
            raise Exception("Didn't find end of JPG!")

        istart += startfix
        iend += endfix
        print("JPG %d from %d to %d" % (njpg, istart, iend))
        jpg = pdf[istart:iend]
        with open("jpg%d.jpg" % njpg, "wb") as jpgfile:
            jpgfile.write(jpg)

        njpg += 1
        i = iend

countJPG = 0

for file in os.listdir(currentDir):
    if file.endswith(".jpg"):
        img = Image.open(file)
        countJPG += 1
        img1 = img.crop((0, 0, 1646, 1165))
##      img1 = img1.resize((basewidth,hsize)
        img1.save("img%d.jpg" % countJPG)
        countJPG += 1
        img2 = img.crop((0, 1165, 1646, 2331))
##      img2 = img1.resize((basewidth,hsize)
        img2.save("img%d.jpg" % countJPG)
        os.remove(file)
