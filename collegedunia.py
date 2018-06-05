

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from urllib.parse import quote


#dtring = 'Management Development Institute (MDI) Gurgaon'

List=pd.read_csv('ColNameList.csv',encoding = "ISO-8859-1")

List=List['Name']

len(List)
#ListU=List[]
p=0
tic=time.time()
List1=[]
for page in List:
    print(str(p)+':'+page)
    url='https://collegedunia.com/e-search?query='+quote(page)+'&c=college'
    try:
        source_code = requests.get(url)
    except:
        toc=time.time()
        break
    
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"lxml")
    data3=soup.find('div',{'class','col-md-4 col-sm-6 lists_wrap'})
    data=data3.find('div',{'class','college_details'})
    List1.append(data.a.get('href'))
    p+=1
    
print(toc-tic,' seconds')
ListFrame = pd.DataFrame(List1)

ListFrame.to_csv('ColDList.csv')