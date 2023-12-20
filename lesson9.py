from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = "https://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

try:

    browser.find_element(By.CSS_SELECTOR, ".btn").click()
    alert = browser.switch_to.alert
    alert.accept()

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x = browser.find_element(By.ID, "input_value").get_attribute("textContent")

    browser.find_element(By.ID, "answer").send_keys(calc(x))
    browser.find_element(By.CSS_SELECTOR, ".btn").click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()