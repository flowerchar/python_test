import time

from selenium import webdriver


def open_browser():
    driver = webdriver.Chrome()
    driver.get("https://ceshiren.com/")
    time.sleep(2)
    driver.refresh()
    driver.get("https://www.baidu.com")
    driver.back()
    driver.maximize_window()
    driver.quit()
    time.sleep(2)


if __name__ == '__main__':
    open_browser()