# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 11:41:05 2018

@author: mayan
"""
from bs4 import BeautifulSoup

import requests

url = "https://www.shiksha.com/mba/colleges/mba-colleges-india"
#url = "https://www.shiksha.com/b-tech/colleges/b-tech-colleges-india"

r  = requests.get(url)

data = r.text

soup = BeautifulSoup(data,'lxml')

table=soup.findAll('div',{'class':'clg-tpl-parent'})
xy={}
sr_no=0
for colg in table:
    data={}
    facilities=[]
    sr_no += 1
    college_name=colg.find('a',{'class':'tuple-institute-name'}).text.split('  ')[0]
#    facilities.append(colg.find('a',{'class':'tuple-institute-name'}).text.split('                ')[0])
    for icon in colg.findAll('li',{'class':'emptyDesc'}):
        facilities.append(icon.h3.text)
    data['Name']=college_name
    data['sr_no']=sr_no
    data['facilities']=facilities
    print(colg.find('div',{'class':'course-inf'}).text)
    print(colg.find('div',{'class':'tuple-fee-col'}).strong.text.strip('\n'))
    try:
        print(colg.find('div',{'class':'tuple-exam-dtls'}).strong.text)
    except:
        pass
    print(colg.find('div',{'class':'tuple-alum-col'}).strong.text.strip())
    
    



#    table=soup.find('li',{'class':'g_lev1'})
linksArray=[]

for row in soup.findAll('a',{'class':'tuple-institute-name'}):
    linksArray.append(row.get('href'))
    

linksArray1 = linksArray

tuple-institute-name
'Asia-Pacific Institute of Management (Delhi)                View college details, courses offered & recommendations\n'
table[0].find('a',{'class':'tuple-institute-name'}).text.split('                ')[0]