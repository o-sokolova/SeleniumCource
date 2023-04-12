from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    submit = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    submit.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    output = browser.find_element(By.CSS_SELECTOR, "#answer")
    output.send_keys(y)

    submit2 = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    submit2.click()
finally:
    time.sleep(10)
    browser.quit()