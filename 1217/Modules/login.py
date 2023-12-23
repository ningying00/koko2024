from Objects.login_page import LoginPage


class Login:
    def login(self, driver, username, password):
        login_page = LoginPage(driver)
        login_page.switch_frame()
        login_page.input_username(username)
        login_page.input_password(password)
        login_page.click_loginBTN()
