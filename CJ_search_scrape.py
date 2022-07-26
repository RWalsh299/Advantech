# Copyright (c) 2022 Advantech GS. All rights reserved.
# Author: Ryan Walsh
# DateCreated: 5/21/22

from selenium import webdriver
from selenium import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time
import csv
#from fake_useragent import UserAgent
from selenium.webdriver.common.keys import Keys
import xlwt
from xlwt import Workbook

def bot():
    # set paths for webdriver + initialize
    options = Options()
    # options.add_argument('--incognito')
    options.binary_location = '/Applications/Google Chrome.app'
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    wb = Workbook()
 
    driver.get('https://www.clearancejobs.com/login')
    time.sleep(1)

    # enter login info
    user = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/form/div/div[2]/div/div/div/input')
    user.send_keys('ptage92121')
    pswd = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/form/div/div[3]/div/div/div/input')
    pswd.send_keys('Advantech2022$')
    driver.find_element_by_xpath('//*[@id="login-btn"]').click()
    
    time.sleep(5)
    #go to search
    driver.get('https://www.clearancejobs.com/resumes/advanced-search/boolean')

    time.sleep(5)
    #insert keywords to search
    keyWords = driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/div/div/div[4]/div/div/textarea')
    keyWords.send_keys("(acquisition OR acquisitions) AND (milestone OR milestones) AND (brief OR briefs OR secnavinst OR 5000) AND (peo OR c4i) AND (ipt OR integrated) AND (risk OR reports OR reporting) AND (documents OR documentation) AND (program OR programs)")
    
    #click search by title OPTIONAL
    #driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div[2]/div/div/div[4]/div/label[2]').click()
    
    time.sleep(2)
    #selecting Clearance lvl

    searchButton = driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/div/div/div[8]/button[2]')
    searchButton.click()
    time.sleep(10)
    
    #Now going through search pages
    pageCount = 1
    sheet1 = wb.add_sheet('S1')
    rowCounter = 0
    while(pageCount <= 10):
        candidates = driver.find_elements_by_class_name('resume-search-candidate-card-desktop')
        for candidate in candidates:
            name = candidate.text
            sheet1.write(rowCounter, 0, name)
            rowCounter+=1
        
        wb.save('CJ_NEW_Scrape.xls')
        pageCount+=1
        time.sleep(10)
        
        """if(pageCount >= 4):
            btn = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[5]/div/div/div/div/div/button[9]')
            btn.click()
        else:
            btn = driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[4]/div/div/div/div/div/button[8]')
            btn.click()
            pageCount += 1"""
    
    wb.save('CJ_NEW_Scrape.xls')

bot()