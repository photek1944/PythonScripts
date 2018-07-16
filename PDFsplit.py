#! python3
# PDFsplit.py | Creates separate PDFs from multi-page PDF file

from PyPDF2 import PdfFileWriter, PdfFileReader
import os, pyperclip

currentDir = pyperclip.paste()
os.chdir(currentDir)

filenameList = os.listdir(currentDir)
print(filenameList)

for i in filenameList:
    if i.lower().endswith('.pdf'):
        inputpdf = PdfFileReader(open(i, "rb"))
        
        for x in range(inputpdf.numPages):
            output = PdfFileWriter()
            output.addPage(inputpdf.getPage(x))
            with open("document-page%s.pdf" % x, "wb") as outputStream:
                output.write(outputStream)
