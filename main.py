# main.py


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from Test_Data.data import Suman_Data
from Test_Locators.locators import Suman_Locators


class Suman:
   
    def __init__(self, url):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get(url)
   
    def login(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.NAME, value=Suman_Locators().username_input_box).send_keys(Suman_Data().username)
        self.driver.find_element(by=By.NAME, value=Suman_Locators().password_input_box).send_keys(Suman_Data().password)
        self.driver.find_element(by=By.XPATH, value=Suman_Locators().submit_button).click()


s = Suman(Suman_Data().url)


s.login()
