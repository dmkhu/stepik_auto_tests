from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from resources import html, vpr

try:
    browser = webdriver.Chrome()

    def registration(my_login, my_password):
        link = "http://stage-fisoko.devl.pro/auth-service/?url=http%3A%2F%2Fstage-fisoko.devl.pro%2Flk"
        browser.get(link)
        login = browser.find_element(By.NAME, "username")
        login.send_keys(my_login)
        password = browser.find_element(By.NAME, "password")
        password.send_keys(my_password)
        button = browser.find_element(By.CSS_SELECTOR, ".v-btn")
        button.click()

    def CreatePublication():
        link = "http://stage-fisoko.devl.pro/lk/admin/publications/create"
        browser.get(link)
        time.sleep(3)

        name_publication = browser.find_element(By.NAME, "name")
        name_publication.send_keys("Тестовая публикация")

        start_at = browser.find_element(By.NAME, "start_at")
        start_at.send_keys("11.12.2023 13:00")

        published_at = browser.find_element(By.NAME, "published_at")
        published_at.send_keys("11.12.2023 13:00")

        description = browser.find_element(By.CSS_SELECTOR, "[name = 'description'] p")
        browser.execute_script(f"arguments[0].innerHTML = '{html}';", description)

        save = browser.find_element(By.CSS_SELECTOR, ".col.col-auto button")
        save.click()

    registration("admin", "fisdevladmin")
    CreatePublication()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(50)
    # закрываем браузер после всех манипуляций
    browser.quit()