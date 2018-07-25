#! python3
# Gendika_DNA.py | Creates separate JPGs from PDF file for Gendika DNA-certificates
# version 2.0

#import modules
import sys, os, pyperclip, glob
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
from PIL import Image

#copy cwd from clipboard
currentDir = pyperclip.paste()

#get filenames
os.chdir(currentDir)

PDFnameList = []
for filename in os.listdir('.'):
   if filename.endswith('.pdf'):
       PDFnameList.append(filename)
PDFnameList.sort(key=str.lower)

#merge pdfs
pdfWriter = PdfFileWriter()

for filename in PDFnameList:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PdfFileReader(pdfFileObj)
    
    for pageNum in range(0, pdfReader.numPages):
               pageObj = pdfReader.getPage(pageNum)
               pdfWriter.addPage(pageObj)
           
pdfOutput = open('merged.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()

#find all images in pdf and convert to jpg
with open("merged.pdf","rb") as file:
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

os.remove('merged.pdf')

#split all jpgs in cwd in two
countJPG = 0
for file in os.listdir(currentDir):
    if file.endswith(".jpg"):
        img = Image.open(file)
        countJPG += 1
        img1 = img.crop((0, 0, 1646, 1165))
        img1.save("img%d.jpg" % countJPG)
        countJPG += 1
        img2 = img.crop((0, 1165, 1646, 2331))
        img2.save("img%d.jpg" % countJPG)
        os.remove(file)
        
#resize all cropped jpgs
countJPG = 0
for file in os.listdir(currentDir):
   print(file)
   if file.endswith(".jpg"):
     countJPG += 1
     img = Image.open(file)
     img_resized = img.resize((1505,1007))
     img_resized.save("dna_resized%d.jpg" % countJPG, quality=97)
     os.remove(file)
