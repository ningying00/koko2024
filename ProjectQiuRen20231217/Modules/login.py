from time import sleep

from selenium import webdriver

from Objects.login_page import LoginPage


class Login:
    def login(self, driver, section, keyword, username, password):
        loginpage = LoginPage(driver)
        loginpage.switch_iframe(section, keyword)
        loginpage.input_username(username)
        loginpage.input_passwor(password)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://mail.163.com/")
    a = Login()
    a.login(driver)
    sleep(5)
