from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


link = "https://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

try:

    browser.find_element(By.NAME, "firstname").send_keys("Dima")
    browser.find_element(By.NAME, "lastname").send_keys("Ivanov")
    browser.find_element(By.NAME, "email").send_keys("ivanov@net.us")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    browser.find_element(By.NAME, "file").send_keys(file_path)

    browser.find_element(By.CSS_SELECTOR, ".btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()