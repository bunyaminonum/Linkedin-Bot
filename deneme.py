from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import time
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

linkList = []
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.get('https://www.kariyer.net/is-ilanlari/?kw=data%20engineer&is=1')
time.sleep(5)
linkList_ = []

def parserList(list:list):
    linkList = []
    for link in list:
        li = str(link).split('/')
        if 'is-ilani' in li and len(link) > 50:
            linkList.append(link)
    return linkList

for number, a in enumerate(driver.find_elements_by_xpath('.//a')):
    Url = a.get_attribute('href')
    linkList.append(Url)

parserList = parserList(linkList)
print(parserList)
for num,i in enumerate(parserList):
    driver.get(i)
    if num == 3:
        time.sleep(5)
        for i in range(10):
            try:
                driver.find_element_by_xpath(
                    "//*[@id='recaptcha-anchor']"
                ).click()
                break
            except NoSuchElementException as e:
                print('Retry in 1 second')
                time.sleep(1)
        else:
            raise e
        break

# willClick = driver.find_element_by_xpath('//*[@id="recaptcha-anchor"]/div[1]')