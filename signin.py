from main import BasePage
from selenium.webdriver.common.by import By
import time

class SignIn(BasePage):
    url = 'https://nuxbet.com/'
    def __init__(self):
        super().__init__()



    def go_to(self):
        self.driver.get(SignIn.url)
        login_btn = self.driver.find_element(By.CLASS_NAME, 'loginBtn')
        login_btn.click()
        time.sleep(5)




    def login(self, username, password):
        name = self.driver.find_element(By.CSS_SELECTOR, 'body > div > div:nth-child(2) > div.modal-mask.authFormPopup > div > div > div > div > form > div:nth-child(1) > div.fieldWrap > input[type=text]')
        name.send_keys(username)
        paswd = self.driver.find_element(By.CSS_SELECTOR, 'body > div > div:nth-child(2) > div.modal-mask.authFormPopup > div > div > div > div > form > div:nth-child(1) > div.passWrap > input[type=password]')
        paswd.send_keys(password)
        time.sleep(3)
        click_log = self.driver.find_element(By.CSS_SELECTOR, 'body > div > div:nth-child(2) > div.modal-mask.authFormPopup > div > div > div > div > form > div.btnWrap > button')
        click_log.click()

        time.sleep(3)

    def logout(self):
        ul_open = self.driver.find_element(By.CSS_SELECTOR, 'body > div > div:nth-child(2) > div > div > div.userBtns.headerItem > div.userWrap.curPointer.logined.allBtn > span.rotateBlockArrow')
        ul_open.click()
        time.sleep(3)
        log_out = self.driver.find_element(By.LINK_TEXT, 'Logout')
        log_out.click()
        time.sleep(3)






