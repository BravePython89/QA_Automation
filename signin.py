from main import BasePage
from selenium.webdriver.common.by import By
import time

class SignIn(BasePage):
    url = 'https://login.nuxgame.com/login'
    def __init__(self):
        super().__init__()

    def go_to(self):
        self.driver.get(SignIn.url)


    def login(self, username, password):
        username = self.driver.find_element(By.NAME, 'email')
        username.send_keys(username)
        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(password)

        go_to_login = self.driver.find_element(By.CLASS_NAME, 'mainBtn')
        go_to_login.click()


    # def check_page(self):
    #     assert self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div[2]/div/div[3]/div[2]/span/span[1]')
