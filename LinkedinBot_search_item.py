import time
import requests
from bs4 import BeautifulSoup
import LinkedinBot_Login
from LinkedinBot_Login import Login
from LinkedinBot_data_manipulation import Manipulation as mn
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

class Search(Login):
    def __init__(self, email:str, password:str, search = 'data engineer', pageNum = 1):
        super().__init__(email, password)
        self.search = mn.splitSearchItem(search)
        self.pageNum = pageNum
        self.empList = []
        self.sepList = []
        self.pList = []
        self.toFloatList = []
        self.linkList = []
        self.average = 0

        Num = [num for num in range(0, self.pageNum * 25 + 1, 25)]
        for num in Num:
            # self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            self.linkList = []
            self.link = f'https://www.linkedin.com/jobs/search/?geoId=102105699&keywords={self.search}&start={num}'
            print(self.link)
            # print(self.linkList)
            print(f"num of job posting: {num}")
            self.driver.get(self.link)

            # r = requests.get(self.link)
            # soup = BeautifulSoup(r.content, 'html.parser')
            # Url = soup.findAll('a')
            a = 1

            for number,a in enumerate(self.driver.find_elements_by_xpath('.//a')):
                Url = a.get_attribute('href')
                self.linkList.append(Url)


            # for number, url in enumerate(Url):
            #     self.linkList.append(url.get('href'))

            # print(self.linkList)
            filteredlinkList_ = mn.linkParser(self.linkList)
            for i in filteredlinkList_:
                print(i)
            # print(filteredlinkList_)
            self.driver.implicitly_wait(10)
            try:
                for link in filteredlinkList_:
                    self.driver.get(link)
                    # time.sleep(0.5)
                    try:
                        #alternative way for 'employee' variable ↓
                        """
                        employee = self.driver.find_element_by_css_selector(
                            'body > div.application-outlet > div.authentication-outlet >'
                            ' div > div.job-view-layout.jobs-details > div.grid > div >'
                            ' div:nth-child(1) > div > div.p5 > div.mt5.mb2 >'
                            ' ul > li:nth-child(2) > span')
                        """
                        company_name = self.driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div[1]/div[1]/div/div[1]/div/div[2]/h1')
                        employee = self.driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/ul/li[2]/span')

                    except:
                        continue
                    changeToTextList = str(employee.text).split()
                    self.empList.append(changeToTextList[0])
                    print(f'{company_name.text}: {changeToTextList[0]}')
            except TimeoutError:
                continue
        self.sepList = mn.parserList(self.empList)
        self.pList = mn.splitAndCheckNum(self.sepList)
        self.emoListt = mn.toFloat(self.pList)
        self.toFloatList = mn.toFloat(self.emoListt)
        self.average = mn.getAvarage(self.toFloatList)



a =Search('19701023@mersin.edu.tr', 'mardin47', 'full stack developer', 2)
print(a.average)
