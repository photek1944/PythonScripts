#! python 3.7
#! convert pdf to jpg through pdf2image module

# 1. install poppler for your windows version -> download zip file from http://blog.alivate.com.au/poppler-windows/
#    and unzip to C:\Program Files (x86)\Poppler

# 2. add 'C:\Program Files (x86)\Poppler\poppler-0.68.0\bin' to SYSTEM PATH environment variable

# 3. from cmd "pip install pdf2image"

# 4. Reboot

import os, pyperclip, tempfile
from pdf2image import convert_from_path
from PIL import Image

#get pdf folder from clipboard
pdf_dir = pyperclip.paste()
os.chdir(pdf_dir)

def jpg_resize(page_img):
    
    width, height = page_img.size
    proportions = 1444 / int(width)
    width = 1444
    height = int(proportions * int(height))

    page_resized = page_img.resize((width,height), Image.ANTIALIAS)
    
    return page_resized

#for each pdf in pdf folder convert to jpg and resize width to 1444px
for pdf_file in os.listdir(pdf_dir):
    
    if pdf_file.endswith(".pdf"):

        with tempfile.TemporaryDirectory() as path:

            pages = convert_from_path(pdf_file, dpi=300, output_folder=path)
        
            print("Converting to JPG: " + pdf_file)
            pdf_file = pdf_file[:-4]

            #conversion for multiple page pdf
            if len(pages) > 1:
            
                for page in pages:

                    if page.size[0] > 1444:
                    
                        page_resized = jpg_resize(page)
                
                        page_resized.save("%s-page%d.jpg" % (pdf_file,pages.index(page)), "JPEG", optimize=True, quality=95)

                    else:

                        page.save("%s-page%d.jpg" % (pdf_file,pages.index(page)), "JPEG", optimize=True, quality=95)
                    
            #conversion for single page pdf
            else:

                for page in pages:

                    if page.size[0] > 1444:
                        
                        page_resized = jpg_resize(page)

                    if pdf_file[-4:] == "_ped":

                        page_resized.save("%s.jpg" % (pdf_file), "JPEG", optimize=True, quality=95)

                    else:
                    
                        page_resized.save("%s_ped.jpg" % (pdf_file), "JPEG", optimize=True, quality=95)

print('Conversion ready!')
