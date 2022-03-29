
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time


class Login:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.link =  'https://www.linkedin.com/login'
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(self.link)
        self.driver.implicitly_wait(10)

        id = self.driver.find_element_by_id('username')
        id.send_keys(self.email)

        id = self.driver.find_element_by_id('password')
        # login = driver.find_element_by_xpath('//*[@id="join-form-submit"]')
        id.send_keys(self.password)
        id.submit()

# l = Login('19701023@mersin.edu.tr', 'mardin')


