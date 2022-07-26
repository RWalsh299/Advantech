# Copyright (c) 2022 Advantech GS. All rights reserved.
# Author: Ryan Walsh
# DateCreated: 5/21/22

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import time
#from fake_useragent import UserAgent
from selenium.webdriver.common.keys import Keys

def bot():
    # set paths for webdriver + initialize
    options = Options()
    # options.add_argument('--incognito')
    options.binary_location = '/Applications/Google Chrome.app'
    driver = webdriver.Chrome(ChromeDriverManager().install())
    count = 0
    driver.maximize_window()
 
    driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
    time.sleep(1)

    # enter login info
    user = driver.find_element_by_xpath('/html/body/div/main/div[2]/div[1]/form/div[1]/input')
    user.send_keys('jack.c.fraser3@gmail.com')
    pswd = driver.find_element_by_xpath('/html/body/div/main/div[2]/div[1]/form/div[2]/input')
    pswd.send_keys('jandc4ever')
    driver.find_element_by_xpath('/html/body/div/main/div[2]/div[1]/form/div[3]/button').click()
    time.sleep(3)
    
    #NEXT TIME YOU RUN PUT KEY WORDS AKA bd OR cAPTURE OR vICE pRES IN THE KEYWORDS BELOW NOT IN THE IF STATMENT BELOW
    page_count = 1
    keywords_search = 'Booz Allen Hamilton'
    
    # time.sleep(5)
    # driver.find_element_by_partial_link_text('all people results').click()
    # time.sleep(5)
    while (page_count != 100):
        driver.get('https://www.linkedin.com/search/results/people/?keywords=' + str(keywords_search) +'&origin=CLUSTER_EXPANSION&page='+ str(page_count) +'')
        time.sleep(7)
        titles = driver.find_elements_by_class_name('reusable-search__result-container ')
        #titles = driver.find_elements_by_xpath('/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[1]/ul/li[1]/div/div/div[2]/div[2]')
        #titles = driver.find_elements_by_class_name('entity-result__summary entity-result__summary--2-linest-12 t-black--light mb1')
        #note:10 connections per page
        li_count = 1
        for title in titles:
            try:
                actions = ActionChains(driver)
                actions.move_to_element(title).perform()
                temp = title.text
                #print(temp)

                if ("Booz" in temp) and ("Business Development" in temp or "BD" in temp or "Capture" in temp or "Vice President" in temp or "VP" in temp or "Chief" in temp or "Program Manager"): # and criteria in temp: #need criteria from pamela
                    #print('here1.5')
                    name = driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/ul/li['+str(li_count)+']/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a/span')
                    name = str(name.text)
                    #print(name)
                    name = name.split(' ')
                    name = name[0]
                    #print("Here2")

                    testButton = driver.find_element_by_xpath('/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[1]/ul/li['+str(li_count)+']/div/div/div[3]/div/button')

                    testButton = str(testButton.text)
                    if(testButton != "Connect"):
                        if(testButton == "Message"):
                            print("Already connected with " +str(name))
                            li_count += 1
                        elif (testButton == "Pending"):
                            print('pending conn for ' + str(name))
                            li_count += 1
                            continue
                        #to do, (this is for button says 'follow') not finished yet 
                        driver.find_element_by_xpath('/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[1]/ul/li['+str(li_count)+']/div/div/div[3]/div/button').click()
                        li_count += 1
                        time.sleep(4)
                        #count += 1
                        try:

                            driver.find_element_by_xpath('/html/body/div[5]/div[3]/div/div/div/div/div[2]/div/div/main/div/section/div[2]/div[3]/div/a').click()

                            msgb = driver.find_element_by_xpath('/html/body/div[5]/aside/div[2]/div[1]/div[4]/div[3]/form/div[3]/div/div/div[1]/p/br')
                            time.sleep(2)
                            msgb.send_keys(name + "Advantech has won 70 contracts with BAH in 15 yrs as a SDVO/HUBZone & TS-FCL exclusive to tech & prof services. We're fortunate to have many BAH VP testimonials! Glad to connect & also support you in staying ahead of market needs. R/ Jack 858.705.3069 www.advantech-gs.com")
                            time.sleep(3)
                            driver.find_element_by_xpath('/html/body/div[5]/aside/div[2]/div[1]/div[4]/div[3]/form/footer/div[2]/div/button').click()
                            driver.execute_script("window.history.go(-1)")

                            time.sleep(2)
                            li_count += 1 #dylan is a female dog

                        except Exception:
                            print('oops')
                            driver.execute_script("window.history.go(-1)")
                            li_count += 1
                            continue
                        #END OF follow BLOCK, not finished yet
                    else:
                        #clicks on the add a note button
                        driver.find_element_by_xpath('/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[1]/ul/li['+str(li_count)+']/div/div/div[3]/div/button').click()

                        driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[1]/span').click()
                        msgb = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/textarea')
                        time.sleep(2)
                        msgb.send_keys(name + " Advantech has won 70 contracts with BAH in 15 yrs as a SDVO/HUBZone & TS-FCL exclusive to tech & prof services. We're fortunate to have many BAH VP testimonials! Glad to connect & also support you in staying ahead of market needs. R/ Jack 858.705.3069 www.advantech-gs.com")
                        time.sleep(3)
                        driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]/span').click()

                        time.sleep(2)
                        li_count += 1
                        print('Connected & sent message to: ' +str(name))
                else:
                    print('incorrect associate')
                    li_count += 1
            except Exception:
                print('failed to find title')
                li_count += 1
                continue
        page_count += 1
        print(count)
bot()