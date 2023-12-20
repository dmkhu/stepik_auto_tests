import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


def Old_test(link):

    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(2)

    browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("test1")
    browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("test2")
    browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("test3")
    # Отправляем заполненную форму
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Проверяем, что смогли зарегистрироваться

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

    return 1


class TestRegistration(unittest.TestCase):
    def test_registration1(self):
        self.assertEqual(Old_test("http://suninjuly.github.io/registration1.html"), 1, "You broke this code!")


    def test_registration2(self):
        self.assertEqual(Old_test("http://suninjuly.github.io/registration2.html"), 1, "You broke this code!")


if __name__ == "__main__":
    unittest.main()