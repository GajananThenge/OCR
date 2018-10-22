# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 21:45:38 2018

@author: hp-pc
"""

from PIL import Image
from pytesseract import image_to_string
tessdata_dir_config=r'C:\Program Files (x86)\Tesseract-OCR\tessdata'
image = Image.open(r'C:\Users\hp-pc\Desktop\image.png', mode='r')
print(image_to_string(image,config=tessdata_dir_config,lang='chi_sim'))
