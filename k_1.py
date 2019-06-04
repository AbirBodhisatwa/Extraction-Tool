# -*- coding: utf-8 -*-
"""
Created on Tue May 21 15:34:32 2019

@author: KAUSTUBH
"""
import numpy as num
filepath = r"C:\\Users\\KAUSTUBH\\Desktop\\AllDicts\\college.txt"
#name=(filepath.split('\\'))
#name=name[-1]
#print(name)


file = open(filepath,"r")
#L=[""]
for line in file:
      #L.append(line)
      print(line)

file.close()
  