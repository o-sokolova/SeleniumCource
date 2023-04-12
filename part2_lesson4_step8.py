from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    output = browser.find_element(By.CSS_SELECTOR, "#answer")
    output.send_keys(y)

    submit = browser.find_element(By.ID, "solve")
    submit.click()
finally:
    time.sleep(10)
    browser.quit()