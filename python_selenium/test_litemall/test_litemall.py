import os
from time import sleep, time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

from python_selenium.test_litemall.utils.log_util import logger


class TestLitemall:

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.product_id = 123
        self.add_name = "测试商品类目1"

        self.driver.get("https://litemall.hogwarts.ceshiren.com")
        ele = self.driver.find_element(By.NAME, "username")
        ele.clear()
        ele.send_keys("manage")
        ele2 = self.driver.find_element(By.NAME, "password")
        ele2.clear()
        ele2.send_keys("manage123")
        # self.driver.find_element(By.CSS_SELECTOR, ".el-button--primary").click()
        self.driver.find_element(By.XPATH, "//*[text()='登录']").click()

    def teardown_class(self):
        self.driver.quit()

    # def test_login(self):
    #     self.driver.get("https://litemall.hogwarts.ceshiren.com")
    #     ele = self.driver.find_element(By.NAME, "username")
    #     ele.clear()
    #     ele.send_keys("manage")
    #     ele2 = self.driver.find_element(By.NAME, "password")
    #     ele2.clear()
    #     ele2.send_keys("manage123")
    #     # self.driver.find_element(By.CSS_SELECTOR, ".el-button--primary").click()
    #     self.driver.find_element(By.XPATH, "//*[text()='登录']").click()

    def test_add_type(self):
        # self.test_login()
        sleep(2)
        self.driver.find_element(By.XPATH, "//*[text()='商品管理']").click()
        self.driver.find_element(By.XPATH, "//*[text()='商品列表']").click()
        sleep(2)
        self.driver.find_element(By.XPATH, "//*[text()='添加']").click()
        sleep(2)
        self.driver.find_elements(By.CLASS_NAME, "el-input__inner")[0].send_keys(self.product_id)
        self.driver.find_elements(By.CLASS_NAME, "el-input__inner")[1].send_keys(self.add_name)
        self.driver.find_element(By.XPATH, "//*[text()='上架']").click()
        sleep(3)
        res = self.driver.find_elements(By.XPATH, f"//*[text()='{self.add_name}']")
        self.get_screen()
        assert res != []
        logger.info("添加商品类目成功")

    def test_delete_type(self):
        # self.test_add_type()

        sleep(2)
        self.driver.find_element(By.XPATH, f"//*[text()='{self.add_name}']/../..//*[text()='删除']").click()
        sleep(2)
        res = self.driver.find_elements(By.XPATH, f"//*[text()='{self.add_name}']")
        self.get_screen()
        assert res == []
        logger.info("删除商品类目成功")

    def get_screen(self):
        timestamp = int(time())
        if not os.path.exists('./images'):
            os.mkdir('./images')
        image_path = f'./images/image_{timestamp}.png'
        self.driver.save_screenshot(image_path)
        allure.attach.file(image_path,name="picture", attachment_type=allure.attachment_type.PNG)
        # 在一般放在断言前后调用
        # 因为用到了allure，那么在命令行中执行：pytest -vs test_litemall.py --alluredir=./report --clean-alluredir
        # 然后执行：allure serve ./report 查看报告