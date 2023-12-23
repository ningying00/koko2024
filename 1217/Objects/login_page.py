from selenium import webdriver
from selenium.webdriver.common.by import By

from Util.read_ini import IniToFile
from Util.tools import locate_element


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.parse = IniToFile()
        self.login_options = self.parse.getSection("163mail_login")

    def switch_frame(self):
        iframe = locate_element(self.driver, By.TAG_NAME, "iframe")
        self.driver.switch_to.frame(iframe)

    def input_username(self, username):
        """
        输入用户名
        :param username:
        :return:
        """
        location_type, location_express = self.login_options["login_page.username"].split(":")
        # locate_element(self.driver, By.NAME, "email").send_keys(username)
        locate_element(self.driver, location_type, location_express).send_keys(username)

    def input_password(self, password):
        locate_element(self.driver, By.NAME, "password").send_keys(password)

    def click_loginBTN(self):
        locate_element(self.driver, By.ID, "dologin").click()

# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(10)
#     driver.get("https://mail.163.com/")
#     driver.maximize_window()
#     loginpage = LoginPage(driver)
#     loginpage.switch_frame()
#     loginpage.input_username("qiuren202312")
#     loginpage.input_password("qiuren12345A")
