import time
from collections.abc import Iterable, Iterator

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# def locat_element(driver, type, express):
#     try:
#         WebDriverWait(driver, 5).until(lambda driver: driver.find_element(type, express))
#     except Exception as e:
#         raise e
#
#     return driver.find_element(type, express)
#
#
# """
# 通过id查找
# 通过name查找
# 通过class name查找
# 通过link text或者partial link text查找（适用于a标签、span标签）
# 通过xpath、css查找
# 通过tag name查找
# """
# driver = webdriver.Chrome()
# driver.find_element('id', '123')
# driver.find_element('name', '123')
# driver.find_element('class name', '223')
# driver.find_element('link text', '123')
# driver.find_element('tag name', 'iframe')
# driver.find_element('xpath', '123')
# """
# 刷新页面
# 前进
# 后退
# 获取当前访问页面的网址
# 获取页面title
# 获取页面源代码
# """
# driver.refresh()
# driver.forward()
# driver.back()
# print(driver.current_url)
# print(driver.title)
# print(driver.page_source)
#
# """
# 窗口最大化
# 当前窗口句柄
# 所有窗口句柄，返回类型为list
# 切换窗口句柄
# """
# driver.maximize_window()
# print(driver.current_window_handle)
# print(driver.window_handles)
# driver.switch_to.window(driver.window_handles[0])
#
# """
# 文本输入
# 文本清空
# 点击
# 控件是否显示
# 控件是否可用
# 获取元素属性
# """
# driver.find_element().send_keys("123")
# driver.find_element().click()
# driver.find_element().clear()
# driver.find_element().is_displayed()
# driver.find_element().is_enabled()
# driver.find_element().is_selected()
# driver.find_element().get_attribute()
# # 鼠标悬浮到某个控件上
# ActionChains(driver).move_to_element("元素定位").perform()
# """
# 进入iframe
# 切换回iframe
# 切换至父级iframe
# """
# driver.switch_to.frame("iframe定位位置")
# driver.switch_to.default_content()
# driver.switch_to.parent_frame()
#
# """
# 显示等待
# 隐式等待
# 强制等待
# """
# WebDriverWait(driver, 10).until(lambda driver: driver.find_element("xxx"))
# driver.implicitly_wait(10)
# time.sleep(5)


# class TestDemo:
#     def __iter__(self):
#         pass
#
#     def __next__(self):
#         pass
#
#
# a = TestDemo()
# print(isinstance(a, Iterable))
# print(isinstance(a, Iterator))



