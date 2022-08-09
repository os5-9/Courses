import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calculation(z):
  return str(math.log(abs(12*math.sin(int(z)))))


driver = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
driver.get(link)

driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

confirm = driver.switch_to.alert
confirm.accept()

x_element = driver.find_element(By.ID, "input_value")
x = x_element.text

answer = calculation(x)
print("answer is" + str(answer))

answer_box = driver.find_element(By.ID, "answer")
answer_box.send_keys(answer)

driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

time.sleep(20)
driver.quit()
