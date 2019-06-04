# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 15:22:32 2017

@author: Bodhisatwa
"""
import time
start_time = time.time()
import Extract_Resume

mypath="C:\\Users\\KAUSTUBH\\Desktop\\AI\\extraction_bodhi\\Resumes_Input"
outputpath="C:\\Users\\KAUSTUBH\Desktop\\AI\\extraction_bodhi\\Resumes_Output"


from os import listdir
from os.path import isfile, join
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for file in files:
    filepath=(join(mypath,file))
    Extract_Resume.Extract_Resume(filepath,outputpath)
    #print(filepath)
    
print("--- %s seconds ---" % (time.time() - start_time))
