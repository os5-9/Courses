import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
driver.get(link)

firstname = driver.find_element(By.NAME, "firstname")
lastname = driver.find_element(By.NAME, "lastname")
email = driver.find_element(By.NAME, "email")
file = driver.find_element(By.NAME, "file")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'тест.txt')
firstname.send_keys("name")
lastname.send_keys("surname")
email.send_keys("test@yandex.ru")
file.send_keys(file_path)
driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

time.sleep(10)
driver.quit()
