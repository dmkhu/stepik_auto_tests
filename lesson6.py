from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

try:


    def calc(num1, num2):
        return str(int(num1) + int(num2))

    num1 = browser.find_element(By.ID, "num1").get_attribute("innerText")
    num2 = browser.find_element(By.ID, "num2").get_attribute("innerText")
    print(num1)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(calc(num1, num2))  # ищем элемент с текстом "Python"

    btn = browser.find_element(By.CSS_SELECTOR, ".btn")
    btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()