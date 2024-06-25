import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def wait_show():
    driver = webdriver.Chrome()
    driver.get('https://vip.ceshiren.com/#/ui_study')
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, "success_btn")))
    driver.find_element(By.ID, "success_btn").click()
    time.sleep(3)
    driver.quit()

if __name__ == '__main__':
    wait_show()