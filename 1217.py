# 进一步优化page object

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def locate_element(driver, type, express):
    try:
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element(type, express))

    except:
        print("123")

    return driver.find_element(type, express)


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://mail.163.com/")
driver.maximize_window()
iframe = locate_element(driver, "tag name", "iframe")
driver.switch_to.frame(iframe)
locate_element(driver, "name", "email").send_keys("judy_ning")
locate_element(driver, "name", "password").send_keys("woaini00@")
locate_element(driver, "id", "dologin").click()
locate_element(driver, "xpath", '//*[@id="_mail_component_76_76"]').click()
locate_element(driver, "class name", "nui-editableAddr-ipt").send_keys("judy_ning@163.com")
locate_element(driver, "xpath",
               "/html/body/div[2]/div[1]/div[2]/div[1]/section/header/div[2]/div[1]/div/div/input").send_keys(
    "123")
locate_element(driver, "xpath", "/html/body/div[2]/div[1]/div[2]/div[1]/section/footer/div[1]/span[2]").click()
