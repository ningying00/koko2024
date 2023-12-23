from configparser import ConfigParser

import openpyxl as openpyxl
from selenium.webdriver.support.wait import WebDriverWait


class Tools:
    def locate_element(self, driver, type, expression):
        """
        改写元素定位方法
        :param driver:
        :param type:
        :param expression:
        :return:
        """
        try:
            WebDriverWait(driver, 10).until(lambda driver: driver.find_element(type, expression))
        except Exception as e:
            raise e
        return driver.find_element(type, expression)

    def read_ini_file(self, config, filepath, section, keyword):
        """
        封装读取ini文件方法
        :return:
        """
        config.read(filepath)
        type, expression = config.get(section, keyword).split(":")
        return type, expression


if __name__ == '__main__':
    t = Tools()
    print(t.read_excel_file("login"))
