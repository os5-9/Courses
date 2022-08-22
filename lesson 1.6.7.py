from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
link = "http://suninjuly.github.io/huge_form.html"
driver.get(link)

elements = driver.find_elements(By.CSS_SELECTOR, "[type='text']")
for element in elements:
    element.send_keys("Мой ответ")

driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

time.sleep(10)
driver.quit()
