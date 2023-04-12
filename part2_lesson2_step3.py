from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/selects1.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text
    sum = int(num1) + int(num2)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_visible_text(str(sum))

    submit = browser.find_element(By.CSS_SELECTOR, ".btn-default")
    submit.click()
finally:
    time.sleep(10)
    browser.quit()
