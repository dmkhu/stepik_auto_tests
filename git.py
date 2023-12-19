from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


link = "https://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)
#browser.implicitly_wait(5)



try:

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))

    browser.find_element(By.ID, "book").click()

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x = browser.find_element(By.ID, "input_value").get_attribute("textContent")

    browser.find_element(By.ID, "answer").send_keys(calc(x))

    browser.find_element(By.ID, "solve").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()