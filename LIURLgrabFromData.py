# Copyright (c) 2022 Advantech GS. All rights reserved.
# Author: Ryan Walsh
# DateCreated: 6/16/22
#
# Takes data (names) in from a .xls (make sure its .xls) and finds the
# linkedIn profile of that name from a google search and saves it in
# a .xls file

import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import csv
from selenium.webdriver.common.keys import Keys
import xlrd
import xlwt
from xlwt import Workbook

def bot():
    # set paths for webdriver + initialize
    options = Options()
    # options.add_argument('--incognito')
    options.binary_location = '/Applications/Google Chrome.app'
    driver = webdriver.Chrome(ChromeDriverManager().install())
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

    #create excel sheet
    wb = Workbook()
    sheet1 = wb.add_sheet('S1')

    #inputing data: 645 entrees
    rb = xlrd.open_workbook(r"C:\Users\Ryan Walsh\Desktop\Bots\emailstouse.xls")
    sheet = rb.sheet_by_index(0)
    row_count = sheet.nrows
    counter = 0

    #opening file to write too
    #wb = Workbook()
    #wsheet = wb.add_sheet('S1')

    while(counter < row_count-1):
    #preforming search
        time.sleep(7)
        cell = sheet.cell(counter, 0)
        driver.get('https://google.com')
        try:
            search_query = driver.find_element_by_name('q')
            search_query.send_keys("'"+ cell.value +"' " 'site:Linkedin.com/in/')
            time.sleep(5)
            search_query.send_keys(Keys.RETURN)
            time.sleep(2)
            results = driver.find_elements_by_css_selector('div.g')
            link = results[0].find_element_by_tag_name("a")
            data = link.get_attribute("href")
            print(data)
            sheet1.write(counter, 0, data)
            counter+=1
            wb.save('CJ_to_LI_urls(4).xls')
        except:
            sheet1.write(counter, 0, 'No person found')
            counter+=1
            wb.save('CJ_to_LI_urls(4).xls')
        time.sleep(5)

bot()