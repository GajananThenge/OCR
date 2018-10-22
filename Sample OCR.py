# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 21:55:34 2018

@author: hp-pc
"""
import os
import tempfile
import subprocess

def ocr(path):
    temp = tempfile.NamedTemporaryFile(delete=False)

    process = subprocess.Popen(['tesseract', path, temp.name],encoding='UTF-8', stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    process.communicate()

    with open(temp.name + '.txt', 'r',encoding='UTF-8') as handle:
        contents = handle.read()

    

    return contents

str = ocr(r'C:\Users\hp-pc\Desktop\image.PNG')
print(str)
