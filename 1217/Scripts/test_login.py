from selenium import webdriver

from Modules.login import Login
from Settings.Config import testDataPath
from Util.read_excel import ExcelParse


class TestCase:
    def test_login(self):
        """
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get("https://mail.163.com/")
        driver.maximize_window()
        a = Login()
        a.login(driver, "qiuren202312", "qiuren12345A")
        """
        try:
            excel_par = ExcelParse()
            excel_par.load_workbook(testDataPath)
            excel_par.get_sheet_by_name("login")

            # 获取行数——执行几次
            rows = excel_par.get_rows_nums()
            # 获取第一行的值
            row1_vaule = excel_par.get_row_value(1)
            # 循环读取每一行的值
            for i in range(2, rows + 1):
                row_value = excel_par.get_row_value(i)
                values = dict(zip(row1_vaule, row_value))
                username = values["username"]
                password = values["password"]
                driver = webdriver.Chrome()
                driver.implicitly_wait(10)
                driver.get("https://mail.163.com/")
                driver.maximize_window()
                a = Login()
                a.login(driver, username, password)
        except Exception as e:
            raise e
