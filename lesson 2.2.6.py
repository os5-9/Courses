from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(z):
  return str(math.log(abs(12*math.sin(int(z)))))


driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/execute_script.html")

x_element = driver.find_element(By.ID, "input_value")
x = x_element.text

answer = calc(x)
print("answer is" + str(answer))

answer_box = driver.find_element(By.ID, "answer")
answer_box.send_keys(answer)

button = driver.find_element(By.TAG_NAME, "button")
driver.execute_script("return arguments[0].scrollIntoView(true);", button)

driver.find_element(By.ID, "robotCheckbox").click()
driver.find_element(By.ID, "robotsRule").click()
driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

time.sleep(10)
driver.quit()
