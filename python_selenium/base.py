from selenium import webdriver


class Base:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()