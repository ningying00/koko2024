from configparser import ConfigParser
from time import sleep

from selenium import webdriver

from Settings.config import iniFilePath
from Utils.tools import Tools


class LoginPage:
    filepath = iniFilePath

    def __init__(self, driver):
        self.driver = driver
        self.locate_element = Tools().locate_element
        self.config = ConfigParser()
        self.read_ini_file = Tools().read_ini_file

    def switch_iframe(self, section, keyword):
        """
        跳入iframe
        :return:
        """
        # 写死定位
        # type = "tag name"
        # expression = "iframe"

        # 从ini文件读取定位
        # config = ConfigParser()
        # config.read(r"F:\python\code\koko2024\ProjectQiuRen20231217\Settings\element_location.ini")
        # type, expression = config.get("location", "iframe").split(":")

        # 调用ini文件读取方法,并参数化定位
        # section = "location"
        # keyword = "iframe"
        type, expression = self.read_ini_file(self.config, LoginPage.filepath, section, keyword)
        iframe = self.locate_element(self.driver, type, expression)

        self.driver.switch_to.frame(iframe)

    def input_username(self, username):
        """
        定位用户名输入框，并输入用户名
        :return:
        """
        type = "name"
        expression = "email"
        self.locate_element(self.driver, type, expression).send_keys(username)

    def input_passwor(self, passwored):
        """
        定位密码输入框，并输入密码
        :return:
        """
        type = "name"
        expression = "password"
        self.locate_element(self.driver, type, expression).send_keys(passwored)

    def button_login(self):
        """
        定位登录按钮，并点击
        :return:
        """
        type = "id"
        expression = "dologin"
        self.locate_element(self.driver, type, expression).click()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://mail.163.com/")
    a = LoginPage(driver)
    a.switch_iframe()
    a.input_username("qiuren202312")
    a.input_passwor("qiuren12345A")
    sleep(5)
