import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/math.html"


@pytest.fixture(autouse=True, scope="class")
def get_x_value():
    print("\n AUTOUSE METHOD")


class TestCaseXValue:
    @classmethod
    def setup_class(self):
        print("\n STARTING DRIVER")
        self.driver = webdriver.Chrome()

    @classmethod
    def teardown_class(self):
        print("\n QUIT DRIVER")
        self.driver.quit()

    def test_x_value_more_than_zero(self):
        self.driver.get(link)
        x_element = self.driver.find_element(By.ID, "input_value")
        x = int(x_element.text)
        assert x > 0, "x value must be more than 0"

    def test_x_value_less_than_thousand(self):
        self.driver.get(link)
        x_element = self.driver.find_element(By.ID, "input_value")
        x = int(x_element.text)
        assert x < 1000, "x value must be less than 1000"
