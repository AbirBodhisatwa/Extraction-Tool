# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 15:02:17 2017

@author: Bodhisatwa
"""

import re
alpha="([A-Za-z]*)?"
space=r"((\s)*)?"
special="(-|/|\.|till|to|'|,|’|–|‘)"


M="(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec|january|february|march|april|may|june|july|august|september|october|november|december)"
A=alpha+space+special+"?"+space+alpha
N="[0-9]"

date=M+A+N+"+"
date2=N+"{1,2}"+special+N+"{1,2}"+special+N+"{2,4}"
date3=N+"{1,2}"+A+M+space+special+"?"+space+N+"{2,4}"
date4=M+A+N+"+"+A+N+"{2,4}"

period=date+A+date
period2=date2+A+date2
period3=date3+A+date3
period4=date4+A+date4

cur_period=date+A+"(till|to)?"+space+"(date|current|present)"
cur_period2="(since|from)"+space+date
cur_period3=date2+A+"(date|current|present)"
cur_period4="(since|from)"+space+date2
cur_period5=date3+A+"(date|current|present)"
cur_period6="(since|from)"+space+date3
cur_period7=date4+A+"(date|current|present)"
cur_period8="(since|from)"+space+date4

Date=re.compile(date,re.IGNORECASE)
Date2=re.compile(date2)
Date3=re.compile(date3,re.IGNORECASE)
Date4=re.compile(date4,re.IGNORECASE)

Period=re.compile(period,re.IGNORECASE)
Period2=re.compile(period2)
Period3=re.compile(period3,re.IGNORECASE)
Period4=re.compile(period4,re.IGNORECASE)

Cur_Period=re.compile(cur_period,re.IGNORECASE)
Cur_Period2=re.compile(cur_period2,re.IGNORECASE)
Cur_Period3=re.compile(cur_period3,re.IGNORECASE)
Cur_Period4=re.compile(cur_period4,re.IGNORECASE)
Cur_Period5=re.compile(cur_period5,re.IGNORECASE)
Cur_Period6=re.compile(cur_period6,re.IGNORECASE)
Cur_Period7=re.compile(cur_period5,re.IGNORECASE)
Cur_Period8=re.compile(cur_period6,re.IGNORECASE)

Qual=re.compile(r"(ACADEMI|QUALIFICATION|EDUCATION)(\w)*(\s)*(\w)*")
Salary=re.compile(r"\d+(.\d+)*(,\d+)*(\w)+")
Notice_Per=re.compile(r"[0-9]{1,2}(\s)*(Months|Month|Weeks|Week|week)")
Exper=re.compile(r"[0-9]{1,2}(\.)?(\d)?(\s)*(Years|years|Months|months|yrs|days)")
Email=re.compile(r'[\w+.+-]+@[\w+-]+\.[\w+-.]+')
Gen=re.compile(r"(Male|Female|male|female|MALE|FEMALE)")
