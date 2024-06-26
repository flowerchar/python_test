import time

from selenium.webdriver.common.by import By

from python_selenium.base import Base

'https://litemall.hogwarts.ceshiren.com/#/dashiboard'

class TestWindows(Base):

    def test_window(self):
        self.driver.get('https://www.baidu.com')
        self.driver.find_element(By.LINK_TEXT, '登录').click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        #
        self.driver.find_element(By.LINK_TEXT, '立即注册').click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.find_element(By.ID, 'TANGRAM__PSP_4__userName').send_keys('username')
        self.driver.find_element(By.ID, 'TANGRAM__PSP_4__phone').send_keys('13952062559')
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.find_element(By.ID, 'TANGRAM__PSP_10__footerULoginBtn').click()
        self.driver.find_element(By.ID, 'TANGRAM__PSP_10__userName').send_keys('username')
        self.driver.find_element(By.ID, 'TANGRAM__PSP_10__password').send_keys('password')
        self.driver.find_element(By.ID, 'TANGRAM__PSP_10__submit').click()
        time.sleep(3)

    def test_fenghuang(self):
        self.driver.get('https://www.ifeng.com/')
        windows = self.driver.window_handles
        print(windows)
        self.driver.find_element(By.LINK_TEXT, '科技').click()
        print(windows)
        print(self.driver.window_handles)
        time.sleep(3)
