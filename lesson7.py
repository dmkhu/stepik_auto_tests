from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select


link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

try:

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x = browser.find_element(By.ID, "input_value").get_attribute("textContent")

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(calc(x))

    browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()

    footer = browser.find_element(By.TAG_NAME, "footer")
    browser.execute_script('arguments[0].style.visibility = \'hidden\'', footer)

    browser.find_element(By.ID, "robotsRule").click()


    browser.find_element(By.CSS_SELECTOR, ".btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()