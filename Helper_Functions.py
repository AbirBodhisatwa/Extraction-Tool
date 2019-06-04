# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 12:57:45 2017

@author: Bodhisatwa
"""

import LANG_DICT
import LOC_DICT   #importing Location dictionary
import INDUS_DICT #importing Industry dictionary
import DEG_DICT
import DESIG_DICT
import datetime
import REGEX_LIB
    
def find_EDG(L): #for finding Email,DOB,Gender
    E=[]
    D=""
    gender=''
       
    for line in L:
        if REGEX_LIB.Email.search(line) is not None:
            #print(line)
            o=REGEX_LIB.Email.search(line)
            E.append(o.group())
        if ('Birth' in line) or ('birth' in line) or ('DOB' in line) or ('D.O.B' in line):
            i=L.index(line)
            if REGEX_LIB.Date3.search(line) is not None:
               o=REGEX_LIB.Date3.search(line)
               D=o.group()
            elif REGEX_LIB.Date3.search(L[i+1]) is not None:
               o=REGEX_LIB.Date3.search(L[i+1])
               D=o.group()
            elif REGEX_LIB.Date4.search(L[i]) is not None:
               o=REGEX_LIB.Date4.search(L[i])
               D=o.group()
            elif REGEX_LIB.Date4.search(L[i+1]) is not None:
               o=REGEX_LIB.Date4.search(L[i+1])
               D=o.group()   
            elif REGEX_LIB.Date2.search(line) is not None:
               o=REGEX_LIB.Date2.search(line)
               D=o.group()
            elif REGEX_LIB.Date2.search(L[i+1]) is not None:
               o=REGEX_LIB.Date2.search(L[i+1])
               D=o.group()   
            elif REGEX_LIB.Date.search(line) is not None:
               o=REGEX_LIB.Date.search(line)
               D=o.group()
            elif REGEX_LIB.Date.search(L[i+1]) is not None:
               o=REGEX_LIB.Date.search(L[i+1])
               D=o.group()  
        if REGEX_LIB.Gen.search(line) is not None:
            o= REGEX_LIB.Gen.search(line)
            gender=o.group()
    return(E,D,gender)   

def find_qual(L):
       indx=0
       NL=[]     
       q=[]       
       for line in L:  
         if REGEX_LIB.Qual.search(line.upper()) is not None:
             indx=L.index(line)
             #n=REGEX_LIB.Qual.search(line.upper())
             #print(n.group()+" "+str(indx))
               
       if len(L)<(indx+10):
           end=len(L)
       else:
           end=indx+10
           
       for i in range(indx,end):
               NL.append(L[i])
       
       for line in NL:
          if ('Office' not  in line) or ('DOS' not in line):
                for w in line.split():
                   if w in DEG_DICT.Degree:
                      q.append(line.lstrip())
                
       if(len(q)==0):
           if(len(NL)>2):
            q.append(NL[1])
            q.append(NL[2])
           elif (len(NL)>1):
            q.append(NL[1])   
       return q               
                         
def achieve(L):
    NL=[]
    RNL=[]
    index=[]
    for line in L: 
     if ('Achieve' in line) or ('ACHIEVE' in line):
         ind=L.index(line)
     elif ('AWARDS' in line) or ('Awards' in line):
         ind=L.index(line)         
         
    for i in range(ind, ind+10):
        NL.append(L[i])
        
    print(NL)
    
    for line in NL:
        if (len(line) is 1):
            index.append(NL.index(line))
            
    print(index)        
    return RNL  

def find_np_lo_s(L): #for finding notice period,location,salary
    np=''
    loc=''
    te=''

    L2=[] #for storing line containing notice period
    L11=[] #for storing each salary line of the file
    sal=[]
    
    for line in L:
     if ('Notice' in line):
         L2.append(line)
         i=L.index(line)
         L2.append(L[i+1])
     for word in LOC_DICT.LOC:
         if (word in line):
             i=L.index(line)
             if(('location' in L[i]) or ('Location' in L[i]) or ('location' in L[i])):
               loc=word
             elif(('location' in L[i-1]) or ('Location' in L[i-1]) or ('location' in L[i-1])):
                 loc=word
             else:
                 loc=word
     
     if ('Salary' in line) or ('salary' in line):
         L11.append(line)
         i=L.index(line)
         L11.append(L[i+1])
     elif ('CTC' in line) or ('ctc' in line):
         L11.append(line)
         i=L.index(line)
         L11.append(L[i+1])            
    
     if ('Experience' in line) or ('experience' in line) or ('EXPERIENCE' in line) or ('expertise' in line):
         if REGEX_LIB.Exper.search(line) is not None:
             o=REGEX_LIB.Exper.search(line)
             te=o.group()
    for line in L2:
        if REGEX_LIB.Notice_Per.search(line) is not None:
            o=REGEX_LIB.Notice_Per.search(line)
            np=o.group()
            
    for line in L11:
       if REGEX_LIB.Salary.search(line) is not None:
           o=REGEX_LIB.Salary.search(line)
           sal.append(o.group())
                                             
    return (sal,np,loc,te)       

def find_L_I_P(L):
    lang=[]
    indus=[]
    indus2=[]
    d=[]
    d1=[]
    var=False
         
    for line in L:  
         for word in LANG_DICT.LANG:
             if word in line:
                lang.append(word)
         for word in INDUS_DICT.Industry:
            if word in line:
                if(('worked' in line) or ('experience' in line)):
                         indus.append(word)
                else:
                    indus2.append(word)
         for word in DESIG_DICT.DESIG:
            if word in line:
                i=L.index(line)
                if ('position' in L[i-1]) or ('Position' in L[i-1]):
                    d.append(word)
                elif ('Designation' in L[i-1]) or ('designation' in L[i-1]):
                    d.append(word)
                elif ('position' in L[i]) or ('Position' in L[i]):
                    d.append(word)
                elif ('Designation' in L[i]) or ('designation' in L[i]):
                    d.append(word)   
                d1.append(word)
                
    if(len(d)==0):
       var=True 
                             
    if not(var):
      for i in d:
          if i=="Company Secretary":
             if 'Secretary ' in d:
              d.remove('Secretary ')    
          elif i=="Assistant Company Secretary":
             if 'Secretary ' in d:
               d.remove('Secretary ')
          elif (i=="Assistant Manager") and ('Manager' in d):
             i1=d.index("Assistant Manager")
             i2=d.index("Manager")
             if(i1>i2):
               d.remove('Manager')                
    
    for i in indus:
      if i in INDUS_DICT.Leg:
         indx=indus.index(i)   
         indus[indx]=indus[indx].replace(indus[indx],"Legal")
      elif i in INDUS_DICT.F:
         indx=indus.index(i)   
         indus[indx]=indus[indx].replace(indus[indx],"Finance")
    indus=set(indus)            
    
    if var:
       d=d1
    
    if(len(indus)==0):
        indus=indus2[0:2]      
        
    return (lang,indus,d)
       
def find_exp(L):
    exp=[]
    for line in L:
        if REGEX_LIB.Period.search(line) is not None:
            o=REGEX_LIB.Period.search(line)
            exp.append(o.group())
        elif REGEX_LIB.Period2.search(line) is not None:
            o=REGEX_LIB.Period2.search(line)
            exp.append(o.group())
        elif REGEX_LIB.Period3.search(line) is not None:
            o=REGEX_LIB.Period3.search(line)
            exp.append(o.group())
        elif REGEX_LIB.Cur_Period.search(line) is not None:
            o=REGEX_LIB.Cur_Period.search(line)
            exp.append(o.group())
        elif REGEX_LIB.Cur_Period2.search(line) is not None:
            o=REGEX_LIB.Cur_Period2.search(line)
            exp.append(o.group())
        elif REGEX_LIB.Cur_Period3.search(line) is not None:
            o=REGEX_LIB.Cur_Period3.search(line)
            exp.append(o.group())
        elif REGEX_LIB.Cur_Period4.search(line) is not None:
            o=REGEX_LIB.Cur_Period4.search(line)
            exp.append(o.group())
        elif REGEX_LIB.Cur_Period5.search(line) is not None:
            o=REGEX_LIB.Cur_Period5.search(line)
            exp.append(o.group())
        elif REGEX_LIB.Cur_Period6.search(line) is not None:
            o=REGEX_LIB.Cur_Period6.search(line)
            exp.append(o.group())      
    return exp    

def find_skill(L):
    p_l=[]
    skill=[]
    s1=[]
    s2=[]
    soft=[]
    roles=[]
    for line in L:
         if ('language' in line) or ('Language' in line):
             for word in LANG_DICT.P_LANG:
                 if word in line:
                     p_l.append(word)
                     #print(word)
         for word in map(str.upper,LANG_DICT.skills):
             if word in line.upper():
                #print(word)
                s1.append(word)
         if(('ANALYSED' in line.upper()) or ('ANALYZED' in line.upper())):
                s2.append(line.lstrip())
         elif ('DEVELOPED' in line.upper()):
                s2.append(line.lstrip())
         for word in LANG_DICT.roles:
             if word in line.upper():
                #print(word)
                roles.append(word)
         for word in LANG_DICT.roles_2:
             if word in line.upper():
                roles.append(line)
         for word in map(str.upper,LANG_DICT.soft):
             if word in line.upper():
                #print(word)
                soft.append(word)     
    if(len(s1)>0):
       skill=s1
    else:
       skill=s2            
    return (p_l,skill,soft,roles)                 
    
def write_output(indus,loc,sal,E,D,gender,np,Lang,pos,q,exp,te,name,outputpath,pl,skill,soft,roles):   
    name=outputpath+"\\Extracted_"+name
    f=open(name,"w") #output file name
  
    indus=set(indus) 
    q=set(q)
    sal=set(sal)
    pl=set(pl)
    skill=set(skill)
    soft=set(soft)
    roles=set(roles)
    pos=list(set(pos))
    E=set(E)
    
    f.write("Industry: ")    
    for i in indus:
       f.write("  "+i)
       
    f.write("\n")
    #print(var)
    if len(pos)>0:    
        f.write("Current Designation: "+pos[0]+"\n")
    if len(pos)>1:
      f.write("Previous Designations:\n")
      for i in range(1,len(pos)):
       f.write(pos[i]+"\n")  
        
        
    f.write("\nCurrent Location: "+loc+"\n")

    for s in sal:
      f.write("Salary: "+s+"\n")
    
    f.write("\n")
    
    f.write("Total Job Experience: "+te+"\n")
    
    f.write("Past Job Experiences: \n")
    
    for e in exp:
        f.write(e+"\n")
        
    f.write("\n")
    
    f.write("Academic Qualifications: \n")
    
    for line in q:
        f.write(line)    
    
    f.write("\n")
        
    if len(skill)!=0:
       f.write("Technical Skills: \n")
       f.write("\n")
       for s in skill:        
         f.write(s.title()+"\n")
         
    
    f.write("\n")
    if len(pl)!=0:    
      f.write("Programming Languages: \n")
      f.write("\n")
      for l in pl:
          f.write(l+"\n")
          
    f.write("\n")    
    if len(soft)!=0:
       f.write("Soft Skills: \n")
       for s in soft:        
         f.write(s.title()+"\n")
        
    
    f.write("\n")    
    if len(roles)!=0:
       f.write("Roles & Responsibilities: \n")
       f.write("\n")
       for s in roles:        
         f.write(s.title()+"\n") 
        
    for e in E:
      f.write("\nEmail: "+e+"\n")
  
    f.write("DOB: "+D+"\n")
    f.write("Gender:"+gender+"\n")        
    f.write("Notice Period:"+np)
    
    if(len(Lang)>0):
      f.write("\nLanguages Known: ")
      for l in Lang:
        f.write(l+" ")
                                    
    f.close()              
