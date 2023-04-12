from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import math
import time

link = "http://suninjuly.github.io/file_input.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    name.send_keys("name")

    lastname = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    lastname.send_keys("lastname")

    email = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    email.send_keys("email")

    file = browser.find_element(By.CSS_SELECTOR, "[name='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    file.send_keys(file_path)

    submit = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    submit.click()
finally:
    time.sleep(10)
    browser.quit()