
import time
import requests
from bs4 import BeautifulSoup
import LinkedinBot_Login
from LinkedinBot_Login import Login
from LinkedinBot_data_manipulation import Manipulation as mn
class Search(Login):
    def __init__(self, email:str, password:str, search = 'data engineer', pageNum = 1):
        super().__init__(email, password)
        self.search = search
        self.pageNum = pageNum
        self.empList = []
        self.sepList = []
        self.pList = []
        self.toFloatList = []
        self.linkList = []
        self.avarage = 0


        Num = [num for num in range(25, self.pageNum * 25 + 1, 25)]
        for num in Num:
            self.link = f'https://www.linkedin.com/jobs/search/?keywords={self.search}&start={num}'
            print(num)
            self.driver.get(self.link)

            r = requests.get(self.link)
            soup = BeautifulSoup(r.content, 'html.parser')
            Url = soup.findAll('a')
            for url in Url:
                self.linkList.append(url.get('href'))
            print(self.linkList)
            filteredlinkList_ = mn.linkParser(self.linkList)
            self.driver.implicitly_wait(10)
            try:
                for j in filteredlinkList_:
                    self.driver.get(j)
                    time.sleep(2.5)
                    try:
                        # employee = self.driver.find_element_by_css_selector(
                        #     'body > div.application-outlet > div.authentication-outlet >'
                        #     ' div > div.job-view-layout.jobs-details > div.grid > div >'
                        #     ' div:nth-child(1) > div > div.p5 > div.mt5.mb2 >'
                        #     ' ul > li:nth-child(2) > span')
                        employee = self.driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/ul/li[2]/span')

                    except:
                        continue
                    changeToTextList = str(employee.text).split()
                    self.empList.append(changeToTextList[0])
                    print(changeToTextList[0])
            except TimeoutError:
                continue
        self.sepList = mn.parserList(self.empList)
        self.pList = mn.splitAndCheckNum(self.sepList)
        self.emoListt = mn.toFloat(self.pList)
        self.toFloatList = mn.toFloat(self.emoListt)
        self.avarage = mn.getAvarage(self.toFloatList)


# a = Search('19701023@mersin.edu.tr', 'mardin47', 'project manager', 1)
# print(a.avarage)
