from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    output = browser.find_element(By.CSS_SELECTOR, "#answer")
    output.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()

    radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()

    submit = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()
finally:
    time.sleep(10)
    browser.quit()