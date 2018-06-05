# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 21:16:13 2018

@author: nikhil
"""
import numpy as np
import requests
from bs4 import BeautifulSoup
import pandas as pd


List3=pd.read_csv('URLList.csv')
List3=List3['0']
xy={}
di={}
sr_no=32076
newlist=List3.copy()
   
college_left = []
for clue in List3:
    college_left.append(clue)
List3=college_left.copy()
for page4 in List3:    
    url4="http://www.htcampus.com"+str(page4)
    source_code4=requests.get(url4)
    plain_text4 = source_code4.text   
    soup4 = BeautifulSoup(plain_text4,"lxml")
    di={}
    key={}
    nm=soup4.find('h1',{'class':'media-heading'})
    u=nm.text
    di['Name']=u.strip()
    List4=[]
    for link4 in soup4.findAll('div',{'class':'grey-gr'}):
        List4.append(link4)
    Key=[]
    Value=[]
    for vl in List4:
        Key.append(vl.find('p',{'class':'text-uppercase f12 c9 text-center'}))
        Value.append(vl.find('span',{'class':'f24'}))
    key=[]
    value=[]
    for i in range(len(Key)):
        if str(type(Key[i]))=="<class 'NoneType'>":
            break
        key.append(Key[i].strong.text)
        di[Key[i].strong.text]=Value[i].text
    try:
        fac=soup4.find_all('ul',{'class':'facilities'})
        List6=[]
        for f in fac[0].findAll('li',{'class':"custom-tabs"}):
            List6.append((f.p.text).strip())
        di['Facility']=List6
    except:
        print("No Value")
    url5=url4+'#courses'
    source_code5=requests.get(url5)
    plain_text5 = source_code5.text   
    soup5 = BeautifulSoup(plain_text5,"lxml")
    cna={}
    courseAll=soup5.findAll('div',{'class':"accordion_example2 smk_accordion acc_with_icon margin-top-30"})        
    course_no=0
    course={}
    Rl={}
    for c in courseAll:
        course_list=c.findAll('div',{'class':"acc_head"})
        course_block=c.findAll('div',{'class':"acc_content"})
        result=0
        for i in range(len(course_list)):
            new_di={}
            new_di = di
            inline = course_block[i].findAll('p',{'class':'text-uppercase f12 c9 padding-bottom-0 inline-block'})
            f24=(course_block[i].findAll('span',{'class':'f24'}))
            for g in range(len(f24)):
                    if("," in f24[g].text):
                        t=f24[g].text
                        new_di["Total Fee"]=t
                        g=g+1
                    else:
                        if('months' in f24[g].text):
                            new_di["Duration"]=f24[g].text
                        else:
                            if(('Time' in f24[g].text) or ('Correspondence' in f24[g].text)):
                                new_di['Course_Type']=f24[g].text            
            new_di['Course']=course_list[i].span.text
            new_di['Course No'] = i
            xy[sr_no]=new_di.copy()
            sr_no +=1
            print(sr_no,new_di['Name'])
            
    college_left.pop(0)
    print('Remaining colleges: ',len(college_left))
    pd.DataFrame(college_left).to_csv("college_type_left.csv")
            
df=pd.DataFrame.from_dict(xy, orient='columns', dtype=None)
df=df.T
df.to_csv('final.csv')
