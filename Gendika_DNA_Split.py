#! python3
# Gendika_DNA_Split.py | Creates separate JPGs from PDF file for Gendika DNA-certificates

import os, pyperclip
from wand.image import Image

currentDir = pyperclip.paste()
os.chdir(currentDir)
filenameList = os.listdir(currentDir)
print(filenameList)

#install version imagemagick 6.9 + C++  (v7 is not supported by wand dependency)
#http://docs.wand-py.org/en/latest/guide/install.html#install-imagemagick-windows
#pip install ghostscript


# Converting first page into JPG
with Image(filename="test1.pdf") as img:
     img.save(filename="temp.jpg")
# Resizing this image
with Image(filename="temp.jpg") as img:
     img.resize(200, 150)
     img.save(filename="thumbnail_resize.jpg")
