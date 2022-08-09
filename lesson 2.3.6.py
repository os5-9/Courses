from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calculation(z):
  return str(math.log(abs(12*math.sin(int(z)))))


driver = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
driver.get(link)

driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

new_window = driver.window_handles[1]
driver.switch_to.window(new_window)

x = driver.find_element(By.ID, "input_value").text

answer = calculation(x)
print("answer is " + str(answer))

answer_box = driver.find_element(By.ID, "answer")
answer_box.send_keys(answer)

driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

time.sleep(20)
driver.quit()
