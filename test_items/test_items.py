import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

wait = 12


def test_check_online_shop_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    res = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert len(res) == 1
