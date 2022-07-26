# Copyright (c) 2022 Advantech GS. All rights reserved.
# Author: Ryan Walsh
# DateCreated: 5/21/22

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import csv
#from fake_useragent import UserAgent
from selenium.webdriver.common.keys import Keys

def bot():
    # set paths for webdriver + initialize
    options = Options()
    # options.add_argument('--incognito')
    options.binary_location = '/Applications/Google Chrome.app'
    driver = webdriver.Chrome(ChromeDriverManager().install())
    f = open(r'C:\Users\Ryan Walsh\Desktop\LinkedinURLS.csv', mode='w')
    writer = csv.writer(f)
    driver.maximize_window()
 
    driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
    time.sleep(1)

    # enter login info
    user = driver.find_element_by_xpath('/html/body/div/main/div[2]/div[1]/form/div[1]/input')
    user.send_keys('jack.c.fraser3@gmail.com')
    pswd = driver.find_element_by_xpath('/html/body/div/main/div[2]/div[1]/form/div[2]/input')
    pswd.send_keys('jandc4ever')
    driver.find_element_by_xpath('/html/body/div/main/div[2]/div[1]/form/div[3]/button').click()
    time.sleep(1)

    driver.get('https://google.com')
    search_query = driver.find_element_by_name('q')
    search_query.send_keys('site:Linkedin.com/in/ AND "Booz Allen Hamilton" AND ("growth" OR "development" OR "sales" OR "strategy" OR "proposal" OR "proposals" OR "capture" OR "partnerships" OR "growth" OR "bd")')
    search_query.send_keys(Keys.RETURN)
    counter = 1
    time.sleep(7)
    while (counter < 150):
        linkedin_urls = driver.find_elements_by_class_name('iUh30')
        linkedin_urls = [url.text for url in linkedin_urls]
        #linkedin_firstNames = driver.find_elements_by_class_name('dyjrff qzEoUe')
        #linkedin_firstNames = [name.txt for name in linkedin_firstNames]

        rcounter = 1
        for linkedin_url in linkedin_urls:
            newUrl = linkedin_url.replace(' › ','/in/')
            writer.writerow([newUrl, rcounter])
            rcounter += 1
        time.sleep(7)
        nextpg = driver.find_element_by_id('pnnext')
        nextpg.click()
        counter += 1
    f.close
    
def fileclean():
    f = open(r'C:\Users\Ryan Walsh\Desktop\LinkedinURLS.csv', mode='w')
    writer = csv.writer(f)

bot()