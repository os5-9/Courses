from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_xpath_form"

driver = webdriver.Chrome()
driver.get(link)

input1 = driver.find_element(By.NAME, "first_name")
input1.send_keys("Ivan")
input2 = driver.find_element(By.NAME, "last_name")
input2.send_keys("Petrov")
input3 = driver.find_element(By.CLASS_NAME, "city")
input3.send_keys("Smolensk")
input4 = driver.find_element(By.ID, "country")
input4.send_keys("Russia")
# пытаемся юзать XPATH, хотя можно просто по типу кнопки...
driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]").click()


time.sleep(30)
driver.quit()
