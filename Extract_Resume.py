# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 20:17:30 2017

@author: Bodhisatwa
"""

import Helper_Functions

def Extract_Resume(file_name,outputpath):
     
  file=open(file_name,"r")
  name=(file_name.split('\\'))
  name=name[-1]
  
  L=[""] #for storing each line of the file 
  
  for line in file:
      L.append(line) #storing the lines of document in the list    
      
  L.append("")
  (E,D,gender)=Helper_Functions.find_EDG(L)
  (sal,np,loc,te)=Helper_Functions.find_np_lo_s(L)
  (Lang,indus,pos)=Helper_Functions.find_L_I_P(L)
  
  q=Helper_Functions.find_qual(L)
  
  exp=Helper_Functions.find_exp(L)
  
  (pl,skill,soft,roles)=Helper_Functions.find_skill(L)
  #for i in exp:
      #print(i)
  #for line in q:  
    #print(line)
  
  #Helper_Functions.achieve(L)
  #print(A)
  Helper_Functions.write_output(indus,loc,sal,E,D,gender,np,Lang,pos,q,exp,te,name,outputpath,pl,skill,soft,roles)

outputpath=r'C:\\Users\\RakeshS\\Downloads\\Processing of Unstructured Documents\\Resumes_Output'    
Extract_Resume(r'C:\\Users\\KAUSTUBH\\Desktop\\AI\\extraction_bodhi',outputpath)  