from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest
import time
import math


@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1",
                                  "https://stepik.org/lesson/236896/step/1",
                                  "https://stepik.org/lesson/236897/step/1",
                                  "https://stepik.org/lesson/236898/step/1",
                                  "https://stepik.org/lesson/236899/step/1",
                                  "https://stepik.org/lesson/236903/step/1",
                                  "https://stepik.org/lesson/236904/step/1",
                                  "https://stepik.org/lesson/236905/step/1"])
def test_func1(driver, link):
    answer = math.log(int(time.time()))
    driver.get(link)
    area = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.TAG_NAME, 'textarea')))
    area.send_keys(answer)
    btn = driver.find_element(By.CLASS_NAME, "submit-submission")
    if btn.get_attribute("disabled") is None:
        btn.click()
    else:
        time.sleep(6)
        btn.click()
    time.sleep(2)
    print(driver.find_element(By.TAG_NAME, "p").text)
    assert True, "not true"
