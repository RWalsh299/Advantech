# Copyright (c) 2022 Advantech GS. All rights reserved.
# Author: Ryan Walsh
# DateCreated: 5/21/22
#
# Notes:
#   -Currently takes 4:23 to finish one page of 20 people, (100 ppl ~ 20min) 11 points per person
#   - Can re work try except block, put saving data on outside so wont not save person if one
#   field cant be found

from selenium import webdriver
from selenium import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time
import csv
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
 
    driver.get('https://www.clearancejobs.com/login')
    time.sleep(1)

    # enter login info
    # pamms info:              lindsey's info:
    # user: ptage92121         user: lmag92037
    # pass: Advantech2022$     pass: Advantech2022$
    
    user = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[1]/form/div[1]/div[1]/div/div/input')
    user.send_keys('lmag92037')
    pswd = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[1]/form/div[1]/div[2]/div/div/input')
    pswd.send_keys('Advantech2022$')
    driver.find_element_by_xpath('//*[@id="login-btn"]').click()
    time.sleep(5)

    #go to search
    driver.get('https://www.clearancejobs.com/resumes/advanced-search/boolean')
    time.sleep(5)

    #insert keywords to search, click search
    keyWords = driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/div/div/div[4]/div/div/textarea')
    keyWords.send_keys('Acquisition')
    time.sleep(20)
       
    searchButton = driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/div/div/div[8]/button[2]')
    searchButton.click()
    time.sleep(7)
    
    #Now going through search pages, creating excel sheet, adding headers
    pageCount = 0
    time.sleep(10)
    counter = 0
    wb = Workbook()
    sheet1 = wb.add_sheet('S1')
    rowCounter = 0
    sheet1.write(rowCounter, 0, "Name")
    sheet1.write(rowCounter, 1, "Phone Number")
    sheet1.write(rowCounter, 2, "E-Mail")
    sheet1.write(rowCounter, 3, "Clearence Level")
    sheet1.write(rowCounter, 4, "Years of Experience")
    sheet1.write(rowCounter, 5, "Open To Relocation?")
    sheet1.write(rowCounter, 6, "Desired Sallary")
    sheet1.write(rowCounter, 7, "Title")
    sheet1.write(rowCounter, 8, "Highest degree")
    sheet1.write(rowCounter, 9, "Military Branch")
    sheet1.write(rowCounter, 10,"Ideal Locations")
    sheet1.write(rowCounter, 11,"Last Profile Update")
    rowCounter+=1
    #looping through search results page by page
    while (pageCount < 50):
        candidate_links = driver.find_elements_by_class_name('resume-search-candidate-card-desktop__name')
        time.sleep(3)
        driver.get(candidate_links[counter].get_attribute('href'))
        time.sleep(3)
        pNumber = ""
        try:
            #Writing Data to Excel Sheet
            name = driver.find_element_by_class_name('profile-name').text

            pNumber = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/div[5]/div/div[1]/div[4]/div/div[2]/div/div[3]/div/div[2]/span').text
            if(pNumber == "No home phone"):
                pNumber = driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[1]/div[5]/div/div[1]/div[4]/div/div[2]/div/div[4]/div/div[2]/span').text
            
            eMail = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/div[5]/div/div[1]/div[4]/div/div[2]/div/div[1]/div/div[2]/a').text
            canTitle = driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[1]/div[1]/div/div[2]/div[2]/div[3]/span').text
            cLevel = driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[1]/div[1]/div/div[2]/div[3]/div[1]/div[2]/div/div[1]/span').text
            YOE = driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[1]/div[5]/div/div[1]/div[2]/div/div[2]/div/div[1]/div/div[2]/span').text
            Relo = driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[1]/div[5]/div/div[1]/div[5]/div/div[2]/div/div[1]/div/div[2]/span').text
            dSallary = driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[1]/div[5]/div/div[1]/div[1]/div/div[2]/div[1]/div[4]/div/div[2]/span').text
            hDegree = driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[1]/div[5]/div/div[1]/div[1]/div/div[2]/div[1]/div[5]/div/div[2]/span').text
            mBranch = driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[1]/div[5]/div/div[1]/div[1]/div/div[2]/div[1]/div[7]/div/div[2]/span').text
            idealLoco = driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[1]/div[5]/div/div[1]/div[5]/div/div[2]/div/div[3]/div/div[2]/span').text
            lastProfUpdate = driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[1]/div[5]/div/div[1]/div[1]/div/div[2]/div[1]/div[1]/div/div[2]/span').text

            sheet1.write(rowCounter, 0, name)
            sheet1.write(rowCounter, 1, pNumber)
            sheet1.write(rowCounter, 2, eMail)
            wb.save('CJ_Scrape(1)_7_15_22.xls')
            sheet1.write(rowCounter, 7, canTitle)
            sheet1.write(rowCounter, 3, cLevel)
            sheet1.write(rowCounter, 6, dSallary)
            sheet1.write(rowCounter, 4, YOE)
            sheet1.write(rowCounter, 8, hDegree)
            sheet1.write(rowCounter, 9, mBranch)
            sheet1.write(rowCounter, 10, idealLoco)
            sheet1.write(rowCounter, 11, lastProfUpdate)
            wb.save('CJ_Scrape(1)_7_15_22.xls')

            time.sleep(2)
            rowCounter+=1
            driver.back()
        except:
            print('Could not find vals')
            driver.back()
        time.sleep(5)

        #Saving Data to excel
        #wb.save('CJ_Data_6_29_22.xls')

        #going to next page
        if(counter / 19 == 1):
            driver.find_element_by_class_name('btn.btn--next').click()
            time.sleep(5)
            pageCount += 1
            counter = 0
        counter+=1

bot()