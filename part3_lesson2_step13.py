from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class SeleniumTests(unittest.TestCase):

    def register(self, link):
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
        input1.send_keys("name")

        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
        input2.send_keys("surname")

        input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
        input3.send_keys("email@bu.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        expected = "Congratulations! You have successfully registered!"
        self.assertEqual(expected, welcome_text, f"{welcome_text} should contain {expected}")
        browser.quit()
    def test_correct_registration(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.register(link)

    def test_uncorrect_registration(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.register(link)

if __name__ == "__main__":
    unittest.main()
