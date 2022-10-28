import requests
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

link = "https://www.linkedin.com/jobs/view/data-engineer-multiple-levels-at-resurety-inc-2971081904/?refId=5LA9K5kDeL%2FftsCRx%2FApfw%3D%3D&trackingId=gvZCdL7MbG%2BRx18eS%2FS%2BHQ%3D%3D&position=11&pageNum=0&trk=public_jobs_jserp-result_search-card"

r = requests.get(link)
bs = BeautifulSoup(r.content, 'html.parser')
links = bs.findAll()
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(link)
for i in links:
    print(i.get('href'))