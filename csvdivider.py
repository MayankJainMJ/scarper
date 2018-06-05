#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 11:49:04 2018

@author: gauravsnr
"""


import numpy as np
import pandas as pd


List3=pd.read_csv('college_type_left.csv')
List3=List3['0']
Listnew=[]
name=1
i=0
while True:
        
    if i+1==len(List3):
        pd.DataFrame(Listnew).to_csv("college_type_left_{}.csv".format(name))
        name += 1
        break
    Listnew.append(List3[i])
    if len(Listnew)==3000:       
        pd.DataFrame(Listnew).to_csv("college_type_left_{}.csv".format(name))
        name += 1
        Listnew=[]
    i +=1
        

    
    