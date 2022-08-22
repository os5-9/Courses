import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestRegister(unittest.TestCase):
    def test_register1(self):
        self.link = "http://suninjuly.github.io/registration1.html"
        self.driver = webdriver.Chrome()
        self.driver.get(self.link)

        self.first = self.driver.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
        self.first.send_keys("first")
        self.second = self.driver.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
        self.second.send_keys("second")
        self.third = self.driver.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
        self.third.send_keys("third")
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        time.sleep(1)
        self.welcome_text_elt = self.driver.find_element(By.TAG_NAME, "h1")
        self.welcome_text = self.welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", self.welcome_text, "Should be equal")
        time.sleep(10)
        self.driver.quit()

    def test_register2(self):
        self.link = "http://suninjuly.github.io/registration2.html"
        self.driver = webdriver.Chrome()
        self.driver.get(self.link)

        self.first = self.driver.find_element(By.CSS_SELECTOR, "[placeholder='Inpput your first name']")
        self.first.send_keys("first")
        self.second = self.driver.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
        self.second.send_keys("second")
        self.third = self.driver.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
        self.third.send_keys("third")
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        time.sleep(1)
        self.welcome_text_elt = self.driver.find_element(By.TAG_NAME, "h1")
        self.welcome_text = self.welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", self.welcome_text, "Should be equal")
        time.sleep(10)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
