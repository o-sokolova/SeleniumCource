from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    output = browser.find_element(By.CSS_SELECTOR, "#answer")
    output.send_keys(y)
    checkbox = browser.find_element(By.CSS_SELECTOR, ".check-input#robotCheckbox")
    checkbox.click()
    radiobutton = browser.find_element(By.CSS_SELECTOR, ".check-input#robotsRule")
    radiobutton.click()
    submit = browser.find_element(By.CSS_SELECTOR, ".btn-default")
    submit.click()
finally:
    time.sleep(10)
    browser.quit()