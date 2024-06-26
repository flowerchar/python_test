import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


class TestKeyboard:

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def teardown_class(self):
        self.driver.quit()

    def test_keyboard(self):
        self.driver.get('https://ceshiren.com')
        self.driver.find_element(By.ID, "search-button").click()
        ele = self.driver.find_element(By.ID, "search-term")
        ActionChains(self.driver).key_down(Keys.SHIFT, ele).send_keys("appium").perform()
        time.sleep(3)

    def test_enter(self):
        self.driver.get('https://www.sogou.com/')
        ele = self.driver.find_element(By.ID, "query")
        ActionChains(self.driver).send_keys("appium").key_down(Keys.ENTER).perform()
        time.sleep(3)

    def test_copy_paste(self):
        self.driver.get('https://ceshiren.com')
        self.driver.find_element(By.ID, "search-button").click()
        ele = self.driver.find_element(By.ID, "search-term")
        command_control = Keys.CONTROL
        (ActionChains(self.driver)
         .key_down(Keys.SHIFT, ele)
         .send_keys("appium!")
        .key_down(Keys.ARROW_LEFT)
        .key_down(command_control)
        .send_keys("xvvv")
         .perform())
        time.sleep(3)

    def test_move_element(self):
        self.driver.get('https://vip.ceshiren.com/#/ui_study/action_chains2')
        ele = self.driver.find_element(By.CLASS_NAME, "menu")
        ActionChains(self.driver).move_to_element(ele).perform()
        self.driver.find_element(By.XPATH, "//*[contains(text(),'管理班')]").click()
        time.sleep(3)

    def test_scroll_to_element(self):
        self.driver.get('https://ceshiren.com')
        ele = self.driver.find_element(By.XPATH, "//*[text()='接口自动化测试方案设计']")
        # self.driver.execute_script("arguments[0].scrollIntoView();", ele)
        ActionChains(self.driver).scroll_to_element(ele).perform()
        time.sleep(10)

