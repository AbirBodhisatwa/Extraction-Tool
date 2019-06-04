# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 01:49:56 2017

@author: Bodhisatwa
"""
import LANG_DICT

ch='y'

while(ch=='y' or ch=='Y'):
   print("Press 1 to add Technical Skills")
   print("Press 2 to add Roles & Responsibilities")
   print("Press 3 to add Soft Skills")
   choice=int(input("Enter Your Choice\t"))
   if choice==1:
       skill=input("Enter New Technical Skill\t")
       if skill.upper() not in map(str.upper,LANG_DICT.skills):
           LANG_DICT.skills.append(skill)
       else:
           print(skill+" is already present in the Skills Dictionary")
   if choice==2:
       skill=input("Enter New Roles and Responsibilities\t")
       if skill.upper() not in map(str.upper,LANG_DICT.roles):
           LANG_DICT.roles.append(skill)
       else:
           print(skill+" is already present in the Roles & Responsiblities Dictionary")
   if choice==3:
       skill=input("Enter New Soft Skills\t")
       if skill.upper() not in map(str.upper,LANG_DICT.roles):
           LANG_DICT.soft.append(skill)
       else:
           print(skill+" is already present in the Soft Skills Dictionary")        
   ch=input("Press Y or y to add more values\t")        
