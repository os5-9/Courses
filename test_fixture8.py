import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime

link = "https://suninjuly.github.io/math.html"


@pytest.fixture(scope="class")
def driver():
    print("\n STARTING DRIVER")
    driver = webdriver.Chrome()
    yield driver
    print("\n QUIT DRIVER")
    driver.quit()


class TestCaseXValue:
    @pytest.mark.ui
    @pytest.mark.xfail(reason="web element has no len")
    def test_for_test(self, driver):
        one = "123"
        assert one.isdigit(), "string must have only digit"

    @pytest.mark.smoke
    @pytest.mark.skip
    def test_x_value_more_than_zero(self, driver):
        driver.get(link)
        x_element = driver.find_element(By.ID, "input_value")
        x = int(x_element.text)
        assert x > 0, "x value must be more than 0"

    @pytest.mark.smoke
    def test_x_value_less_than_thousand(self, driver):
        driver.get(link)
        x_element = driver.find_element(By.ID, "input_value")
        x = int(x_element.text)
        assert x < 1000, "x value must be less than 1000"
