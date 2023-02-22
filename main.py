import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class BasePage:
    path = r'C:\Users\User\PycharmProjects\Nux_game_test\chromedriver.exe'
    def __init__(self):
        self.driver = webdriver.Chrome(
            service=Service(BasePage.path)
        )
    def close(self):
        self.driver.close()