# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 17:40:27 2018

@author: nikhil
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
os.chdir('/home/gauravsnr/Desktop/scraper')
##Getting List of Colleges##
#################################################################################################


url = "http://www.htcampus.com/" #+ str(page)
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text,"lxml")
List=[]

di={}
xy={}
for link in soup.findAll('a',{'class':'white-box'}):
    href = link.get('href')
    print(href)
    List.append(href)   
List2=[]        
for page in List:
    url2 = "http://www.htcampus.com/" + str(page)
    source_code2 = requests.get(url2)
    plain_text2 = source_code2.text   
    soup2 = BeautifulSoup(plain_text2,"lxml")
    for link2 in soup2.findAll('a',{'class':'discussion-box'}):
        href2 = link2.get('href')
        #print(href2)
        List2.append(href2)    

print(len(List2))
College_types=pd.DataFrame(List2)
College_types.to_csv("College_types.csv")
college_left = List2.copy()
#college_left = pd.read_csv("College_left.csv")
newlist=List2.copy()

List2 = college_left.copy()
List3=[]
for page2 in List2:
    
    url3="http://www.htcampus.com/"+str(page2)
    source_code3=requests.get(url3)
    plain_text3 = source_code3.text   
    soup3 = BeautifulSoup(plain_text3,"lxml")
    p=1
    if page2=='/engineering/ece-electronics-communication-engineering-colleges-in-india/':
        p=42
    urlCollege=url3+"?page="+str(p)
    source_codeC=requests.get(urlCollege)
    plain_textC = source_codeC.text   
    soupC = BeautifulSoup(plain_textC,"lxml")
    soupC.findAll('ul',{'class':'pagination'})
    while True:
        urlCollege=url3+"?page="+str(p)
        source_codeC=requests.get(urlCollege)
        plain_textC = source_codeC.text   
        soupC = BeautifulSoup(plain_textC,"lxml")
        try:
            active_pg = int(soupC.findAll('ul',{'class':'pagination'})[0].findAll('li',{'class':'active'})[0].a.text)
            if  active_pg < p:
                break
            print("You are in page: "+str(active_pg))        
            for link3 in soupC.findAll('a',{'class':'f20 text-semi'}):
                href3 = link3.get('href')
                #print(href3)
                List3.append(href3)
            p=p+1
        except:
            break
    college_left.pop(0)
    pd.DataFrame(college_left).to_csv("college_type_left.csv")
    
URLData=pd.DataFrame(List3)
URLData.to_csv("URLList.csv")