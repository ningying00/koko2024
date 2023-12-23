from selenium.webdriver.support.wait import WebDriverWait


def locate_element(driver, type, express):
    try:
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element(type, express))
    except Exception as e:
        raise e
    return driver.find_element(type, express)
