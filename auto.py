import requests

# for webscapping
from bs4 import BeautifulSoup
import re
import sys
# automation
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('C:/Users/p.kontos/Downloads/chromedriver.exe')
        
url = 'https://www.youtube.com/'

driver.get(url)

driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[5]/div[2]/ytd-button-renderer[2]/a').click()

time.sleep(1)

driver.find_element_by_name("search_query").send_keys("Blues")
driver.find_element_by_id("search-icon-legacy").click()

time.sleep(1)
driver.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string').click()

time.sleep(8)
driver.find_element_by_xpath('//*[@id="skip-button:5"]/span/button').click()


# Scrapping
# extract hacker news and jobs 
def scrappe_news():        
    print('Hacker news')
    url = 'https://news.ycombinator.com/'
    cnt = ''
    cnt += ('HN top stories:\n'+'-'*50+'\n')
    r = requests.get(url)
    content = r.content
    soup = BeautifulSoup(content, 'html.parser')
    for i,tag in enumerate(soup.find_all('td', attrs={'class':'title', 'valign':''})):
        cnt += ((str(i)+' :: '+tag.text + "\n"))
    print(cnt)

def scrappe_jobs():
    url = 'https://www.remotepython.com/jobs/?job_type=fulltime'
    str = ''
    str += 'Python Jobs:\n' + '-'*60+'\n'
    r = requests.get(url)
    content = r.content
    soup = BeautifulSoup(content, 'html.parser')
    for i in (soup.find_all('h3')):
        str += (i.get_text() + '\n')
    print(str)
    

