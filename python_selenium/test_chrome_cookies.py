from time import sleep

from selenium import webdriver
from yaml import safe_dump, safe_load


class TestChromeCookies:

    def setup_class(self):
        self.driver = webdriver.Chrome()

    def test_get_cookies(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contracts")
        sleep(20)
        cookies = self.driver.get_cookies()
        with open("cookies.yaml", "w") as f:
            safe_dump(cookies, f)
        print(cookies)

    def test_add_cookies(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        with open("cookies.yaml") as f:
            cookies = safe_load(f)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        sleep(10)