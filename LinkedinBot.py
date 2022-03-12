import requests
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

class LinkedinBot():
    def __init__(self,search):
        self.link = 'https://www.linkedin.com/login'
        self.search = search
        self.empList = []
        self.pList = []
        self.sepList = []
        self.emoListt = []
        self.avarage = 0
        self.tofloat = []
        self.main()

    def main(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(self.link)
        driver.implicitly_wait(10)

        id = driver.find_element_by_id('username')
        id.send_keys('19701023@mersin.edu.tr')

        id = driver.find_element_by_id('password')
        # login = driver.find_element_by_xpath('//*[@id="join-form-submit"]')
        id.send_keys('mardin47')
        id.submit()

        driver.implicitly_wait(10)
        Num = [i for i in range(25, 26, 25)]
        for num in Num:
            self.link = f'https://www.linkedin.com/jobs/search/?keywords={self.search}&start={num}'
            print(num)
            driver.get(self.link)

            r = requests.get(self.link)
            soup = BeautifulSoup(r.content, 'html.parser')
            Url = soup.findAll('a')
            linkList = []
            for url in Url:
                linkList.append(url.get('href'))
            print(linkList)
            filteredlinkList_ = self.linkParser(linkList)
            driver.implicitly_wait(10)
            print(len(filteredlinkList_))
            try:
                for j in filteredlinkList_:
                    driver.get(j)
                    time.sleep(3)
                    employee = driver.find_element_by_css_selector(
                        'body > div.application-outlet > div.authentication-outlet >'
                        ' div > div.job-view-layout.jobs-details > div.grid > div >'
                        ' div:nth-child(1) > div > div.p5 > div.mt5.mb2 >'
                        ' ul > li:nth-child(2) > span')

                    changeToTextList = str(employee.text).split()
                    self.empList.append(changeToTextList[0])
                    print(self.empList)
            except:
                continue

        self.sepList = self.parserList(self.empList)
        print('************')
        print(self.sepList)
        print('*****************')
        self.pList = self.splitAndCheckNum(self.sepList)
        print(self.pList)
        self.emoListt = self.toFloat(self.pList)
        self.tofloat = self.toFloat(self.emoListt)
        self.avarage = self.getAvarage(self.tofloat)
        # print(se)
        # return self.avarage


    def parserList(self ,list):
        newList = []
        print(list)
        for li in list:
            if ',' in li:
                li = li.replace(',', '')
            if '+' in li:
                li = li[:-1]
            newList.append(li)
        return newList

    def splitAndCheckNum(self, list_: list):
        newList = []
        for i in list_:
            splt = str(i).split('-')
            if len(splt) == 2:
                newList.append(splt[1])
            if len(splt) == 1:
                newList.append(splt[0])
        return newList

    def getAvarage(self, floatList):
        avarage = (sum(floatList) / len(floatList)) / 2
        return avarage

    def linkParser(self, linkList):
        newList = []
        for li in linkList:
            li2 = str(li).split('/')
            if 'view' in li2:
                newList.append(li)
        return newList

    def toFloat(self, list_):
        floatList = []
        for li in list_:
            try:
                li = float(li)
                floatList.append(li)
            except:
                continue
        return floatList



bot = LinkedinBot('java developer')
print(bot.avarage)

