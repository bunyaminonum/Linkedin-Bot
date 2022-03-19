import requests
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time


def parserList(list:list) -> list:
    newList = []
    print(list)
    for li in list:
        if ',' in li:
            li = li.replace(',','')
        if '+' in li:
            li = li[:-1]
        newList.append(li)
    return  newList

def splitAndCheckNum(list_:list) -> list:
    newList = []
    for i in list_:
        splt = str(i).split('-')
        if len(splt) == 2:
            newList.append(splt[1])
        if len(splt) == 1:
            newList.append(splt[0])
    return newList

def toFloat(list_):
    newList = [float(li) for li in list_]
    return newList

def getAvarage(floatList):
    avarage = (sum(floatList)/len(floatList))/2
    return avarage


def linkParser(linkList):
    newList = []
    for li in linkList:
        li2 = str(li).split('/')
        if 'view' in li2:
            newList.append(li)
    return newList

def toFloat(list):
    floatList = [float(num) for num in list]
    return floatList


def findJob(search):
    link = 'https://www.linkedin.com/login'
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(link)
    driver.implicitly_wait(10)

    id = driver.find_element_by_id('username')
    id.send_keys('19701023@mersin.edu.tr')

    id = driver.find_element_by_id('password')
    # login = driver.find_element_by_xpath('//*[@id="join-form-submit"]')
    id.send_keys('mardin47')
    id.submit()

    driver.implicitly_wait(10)
    Num = [i for i in range(25,26,25)]
    empList = []
    for num in Num:
        link = f'https://www.linkedin.com/jobs/search/?keywords={search}&start={num}'
        print(num)
        driver.get(link)

        r = requests.get(link)
        soup = BeautifulSoup(r.content, 'html.parser')
        Url = soup.findAll('a')
        linkList = []
        for url in Url:
            linkList.append(url.get('href'))
        print(linkList)
        filteredlinkList_ = linkParser(linkList)
        driver.implicitly_wait(10)
        print(len(filteredlinkList_))
        for j in filteredlinkList_:
            driver.get(j)
            time.sleep(3)
            employee = driver.find_element_by_css_selector('body > div.application-outlet > div.authentication-outlet >'
                                                           ' div > div.job-view-layout.jobs-details > div.grid > div >'
                                                           ' div:nth-child(1) > div > div.p5 > div.mt5.mb2 >'
                                                           ' ul > li:nth-child(2) > span')

            changeToTextList = str(employee.text).split()
            empList.append(changeToTextList[0])
            print(empList)


    sepList = parserList(empList)
    print('************')
    print(sepList)
    print('*****************')
    pList = splitAndCheckNum(sepList)
    print(pList)
    emoListt = toFloat(pList)
    tofloat = toFloat(emoListt)
    avarage = getAvarage(tofloat)
    return avarage, emoListt


print(findJob('data engineer'))

