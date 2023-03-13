# Use Pytest using Page Object Model

# testSuman.py


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from Test_Data.data import Suman_Data
from Test_Locators.locators import Suman_Locators
import pytest


class Test_Suman:


    #Booting method for running the Pytest test cases
    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        yield
        self.driver.close()
   
    def test_get_title(self, boot):
        self.driver.implicitly_wait(10)
        self.driver.get(Suman_Data().url)
        assert self.driver.title == 'suman'
        print("SUCCESS : Web Title Captured")
   
    def test_login(self, boot):
        self.driver.get(Suman_Data().url)
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.NAME, value=Suman_Locators().username_input_box).send_keys(Suman_Data().username)
        self.driver.find_element(by=By.NAME, value=Suman_Locators().password_input_box).send_keys(Suman_Data().password)
        self.driver.find_element(by=By.XPATH, value=Suman_Locators().submit_button).click()
        assert self.driver.title =='OrangeHRM'
        print("SUCCESS : Logged in with the Username {a} & {b}".format(a=Suman_Data().username, b=Suman_Data().password))