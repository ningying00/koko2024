from selenium import webdriver


class TestDemo:
    def setup(self):
        self.driver = webdriver.Chrome()
        # 隐式等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_01(self):
        self.driver.get("http://www.baidu.com/")
