import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


@pytest.mark.parametrize('stepic_link', ["https://stepik.org/lesson/236895/step/1",
                                         "https://stepik.org/lesson/236896/step/1",
                                         "https://stepik.org/lesson/236897/step/1",
                                         "https://stepik.org/lesson/236898/step/1",
                                         "https://stepik.org/lesson/236899/step/1",
                                         "https://stepik.org/lesson/236903/step/1",
                                         "https://stepik.org/lesson/236904/step/1",
                                         "https://stepik.org/lesson/236905/step/1"])
def test_stepic_auth(browser, stepic_link):
    wait = 12
    browser.get(stepic_link)

    login_button = WebDriverWait(browser, wait).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".navbar__auth"))
    )
    login_button.click()
    login = ""
    psw = ""

    login_field = browser.find_element(By.ID, "id_login_email")
    login_field.send_keys(login)
    psw_field = browser.find_element(By.ID, "id_login_password")
    psw_field.send_keys(psw)
    ok_button = browser.find_element(By.CSS_SELECTOR, ".sign-form__btn")
    ok_button.click()
    assert WebDriverWait(browser, wait).until_not(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".sign-form__body"))
    ) is True

    browser.implicitly_wait(10)
    text_area = browser.find_element(By.CSS_SELECTOR, ".ember-text-area")
    text_area.clear()
    text_area.send_keys(math.log(int(time.time())))

    btn = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
    btn.click()

    res = WebDriverWait(browser, wait).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
    result = res.text
    assert result == "Correct!"
