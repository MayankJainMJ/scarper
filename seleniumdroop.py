# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 11:10:00 2018

@author: mayan
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
#from selenium.webdriver.firefox.options import Options
from time import sleep

driver_path = 'C:/Users/mayan/Desktop/scraper/chromedriver'
fire_path = 'C:/Users/mayan/Desktop/scraper/geckodriver'
phantom_path = 'C:/Users/mayan/Desktop/scraper/phantomjs-2.1.1-windows/bin/phantomjs'
def find_between_exact( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""


def find_between( s, first, last ):
    text=[]
    i=10
    while i >0:
        try:
            start = s.index( first ) + len( first )
            end = s.index( last, start )
            if s[start:end]!='':
                text.append(s[start:end].strip())
            s=s[end+1:]
        except: pass
        i -= 1        
    return text


def Webcall(url):
    # Specifying incognito mode as you launch your browser[OPTIONAL]
#    option = webdriver.ChromeOptions()

    
    option = webdriver.firefox.options.Options()
    option.add_argument("--incognito")
#    option.add_argument("--headless")

    
#    firefox_profile = webdriver.FirefoxProfile()
#    firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
    
    # Create new Instance of Chrome in incognito mode
#    browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
    browser = webdriver.Firefox(executable_path=fire_path,firefox_options=option)
#    browser = webdriver.PhantomJS(executable_path=phantom_path)    
    # Go to desired website
    browser.get(url)
    

        
    titles_element = browser.find_elements_by_xpath("//div[@class='outerframe']")
    for button in titles_element:
        num = find_between_exact(button.get_attribute('outerHTML'),'id="','"')
        print(num)
        try:
            browser.find_elements_by_id(num)[0].click()
            sleep(1)
        except: pass
    data=browser.page_source
    browser.quit()
    return data