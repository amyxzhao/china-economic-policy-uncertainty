# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 10:11:07 2018

@author: dingqian sara
"""
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import numpy as np
from selenium.webdriver.common.action_chains import ActionChains

#import sys
#print(sys.path)  to find system Path

# set default directory
path = r'C:\Users\Yan\Desktop\EPU\RMRB_2008-2016'
os.chdir (path)

# open a testing chrome window
driver = webdriver.Chrome('D:\\python\\lib\\site-packages\chromedriver.exe')

# log in to the library website
driver.get("https://library.georgetown.edu/") # change to GU lib link (virtual)
time.sleep(5)
#driver.switch_to.default_content()
#driver.switch_to.frame('navigate')
#years = driver.find_elements_by_xpath("//a[@target = 'self']")

#years = years.find_elements_by_xpath('//a[@href]')

#time.sleep(10)
#m = years[33].get_attribute('href')
#years[32].click()

# find the page numbers and article numbers
year = '2007'
month='01'
day=[]

for b0 in range(1,32):
    if b0<10:
        b0='0'+str(b0)
        day.append(b0)
    else:
        b0=str(b0)
        day.append(b0)

date = [year + month + f for f in day]

for i in date:
    url0 = 'http://data.people.com.cn.proxy.library.georgetown.edu/rmrb/'+i+'/1'  # Change the link to GU website
    driver.switch_to.window(driver.window_handles[0]) # which tab in the window
    driver.get(url0)
    time.sleep(np.random.uniform(2.4,8,1)[0])
    
    driver.switch_to.default_content()
    page_num = int(driver.find_element(by=By.XPATH, value="//span[@id = 'UseRmrbPageNum']").text)
    arti_num = int(driver.find_element(by=By.XPATH, value="//span[@id = 'UseRmrbNum']").text)
    page0 = list(range(1,page_num+1))
    page0 = [str(f) for f in page0]

    for m in page0:
        url = 'http://iffxbb32508ebed3c4b91hvbkv6cov9w5p6fp0.fgcz.libproxy.ruc.edu.cn/rmrb/'+i+'/'+m
        driver.switch_to.window(driver.window_handles[0])
        driver.get(url)
        driver.switch_to.default_content()
        time.sleep(np.random.uniform(2.4,8,1)[0])
        # find
        links = driver.find_element(by=By.XPATH, value="//div[@class = 'title_list']")
        links = links.find_elements(by=By.XPATH, value="//a[@href]")
      
        #  for i in links:
        #      print(i.get_attribute('href'))

        articles = [ f for f in links if not 'pic' in str(f.get_attribute('href'))]
        articles = [ f for f in articles if not '#' in str(f.get_attribute('href'))]
        articles = articles[3:]
        articles = [str(f.get_attribute('href')) for f in articles ]

        article = [f for f in articles if (len(f)==119 or len(f)>119)]
        article = list(set(article))

    
        driver.execute_script("window.open('');") #new tab

        for n in article:
            driver.switch_to.window(driver.window_handles[-1])
            driver.get(n)
            a = ActionChains(driver)
            driver.switch_to.default_content()
            content = driver.find_element(by=By.XPATH, value = "//div[@class='detail_con']")
            a.move_to_element(content).perform()
            title = driver.find_element(by=By.XPATH, value = "//div[@class='title']")
            a.move_to_element(title).perform()
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(np.random.uniform(1,4,1)[0])
            with open(i +'.txt', 'a', encoding = 'utf8') as f:
                f.write(i +'\n' + title.text +'\n' + content.text+'\n' )
                time.sleep(np.random.uniform(8,20,1)[0])
        driver.close()
        time.sleep(np.random.uniform(1,6,1)[0])

# if break on an article
article.index(n)
len(article)
for n in article[1:]:
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(n)
    driver.switch_to.default_content()
    a = ActionChains(driver)
    content = driver.find_element(by=By.XPATH, value = "//div[@class='detail_con']")
    a.move_to_element(content).perform()
    title = driver.find_element(by=By.XPATH, value = "//div[@class='title']")
    a.move_to_element(title).perform()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(np.random.uniform(2,6,1)[0])
    with open(i +'.txt', 'a', encoding = 'utf8') as f:
        f.write(i +'\n' + title.text +'\n' + content.text +'\n' )
        time.sleep(np.random.uniform(10,20,1)[0])

# if breake on a page
page0.index(m)
len(page0)
for m in page0[3:]:
    url = 'http://iffxbb32508ebed3c4b91hvbkv6cov9w5p6fp0.fgcz.libproxy.ruc.edu.cn/rmrb/'+i+'/'+m
    driver.switch_to.window(driver.window_handles[0])
    driver.get(url)
    driver.switch_to.default_content()
    time.sleep(np.random.uniform(2.4,8,1)[0])
    # find
    links = driver.find_element(by=By.XPATH, value="//div[@class = 'title_list']")
    links = links.find_elements(by=By.XPATH, value="//a[@href]")
      
    #  for i in links:
    #      print(i.get_attribute('href'))

    articles = [ f for f in links if not 'pic' in str(f.get_attribute('href'))]
    articles = [ f for f in articles if not '#' in str(f.get_attribute('href'))]
    articles = articles[3:]
    articles = [str(f.get_attribute('href')) for f in articles ]

    article = [f for f in articles if (len(f)>119 or len(f)==119)]
    article = list(set(article))

    
    driver.execute_script("window.open('');") #new tab

    for n in article:
        driver.switch_to.window(driver.window_handles[-1])
        driver.get(n)
        driver.switch_to.default_content()
        a = ActionChains(driver)
        content = driver.find_element(by=By.XPATH, value = "//div[@class='detail_con']")
        a.move_to_element(content).perform()
        title = driver.find_element(by=By.XPATH, value = "//div[@class='title']")
        a.move_to_element(title).perform()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(np.random.uniform(2,6,1)[0])
        with open(i +'.txt', 'a', encoding = 'utf8') as f:
            f.write(i +'\n' + title.text +'\n' + content.text +'\n' )
            time.sleep(np.random.uniform(8,20,1)[0])
    driver.close()
    time.sleep(np.random.uniform(1,6,1)[0])