from selenium import webdriver

from selenium.webdriver.common.by import By
import math

def calc(z):
  return str(math.log(abs(12*math.sin(int(z)))))


driver = webdriver.Chrome()
driver.get("https://suninjuly.github.io/math.html")

x_element = driver.find_element(By.ID, "input_value")
x = x_element.text

answer = calc(x)

answer_box = driver.find_element(By.ID, "answer")
answer_box.send_keys(answer)

driver.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']").click()
driver.find_element(By.CSS_SELECTOR, "[for='robotsRule']").click()
driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
driver.quit()
