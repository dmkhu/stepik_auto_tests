from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = "https://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

try:


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    find_x = browser.find_element(By.ID, "treasure")
    x = find_x.get_attribute("valuex")

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(calc(x))

    robotCheckbox = browser.find_element(By.ID, "robotCheckbox")
    robotCheckbox.click()

    robotsRule = browser.find_element(By.ID, "robotsRule")
    robotsRule.click()

    btn = browser.find_element(By.CSS_SELECTOR, ".btn")
    btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()