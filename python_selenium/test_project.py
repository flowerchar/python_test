import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCeshiren:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_search(self):
        self.driver.get('https://ceshiren.com/search?expanded=true')
        self.driver.find_element(By.XPATH, "//*[@placeholder='搜索']").send_keys("appium")
        # time.sleep(3)
        # self.driver.find_element(By.XPATH, "//*[contains(text(),'搜索')]").click()
        # self.driver.find_elements(By.XPATH, '//*[@aria-label="搜索"]')[1].click()
        self.driver.find_element(By.CSS_SELECTOR, ".search-cta span").click()
        web_element = self.driver.find_element(By.CLASS_NAME, "topic-title")
        assert "appium" in web_element.text.lower()



    def teardown(self):
        self.driver.quit()