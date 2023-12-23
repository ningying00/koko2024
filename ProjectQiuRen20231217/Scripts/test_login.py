from time import sleep

import openpyxl
from selenium import webdriver

from Modules.login import Login
from Settings.config import excelFilePath
from Utils.read_excel import ReadExcel


class TestLogin:
    def setup(self):
        self.driver = webdriver.Chrome()
        # self.driver.get("https://mail.163.com/")

    def test_login(self):
        # Login().login(self.driver, "login_page", "iframe", "qiuren202312", "qiuren12345A")

        # 从excel读取username，password
        wb = ReadExcel()
        wb.load_excel(excelFilePath)
        wb.get_sheet("login")
        rows = wb.get_row_max()
        keyword = wb.get_row_value(1)
        for i in range(2, rows + 1):
            value = wb.get_row_value(i)
            a = dict(zip(keyword, value))
            username = a['username']
            password = a['password']
            self.driver.get("https://mail.163.com/")
            Login().login(self.driver, "login_page", "iframe", username, password)

