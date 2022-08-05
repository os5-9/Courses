from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import math


def calculation(z):
  return str(math.log(abs(12*math.sin(int(z)))))


chrome_options = Options()
chrome_options.add_argument('--no-sandbox')

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/get_attribute.html")

x_element = driver.find_element(By.ID, "treasure")
x = x_element.get_attribute("valuex")
print("x = " + str(x))

answer = calculation(x)

answer_box = driver.find_element(By.ID, "answer")
answer_box.send_keys(answer)

driver.find_element(By.ID, "robotCheckbox").click()
driver.find_element(By.ID, "robotsRule").click()
driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

time.sleep(1000)
driver.quit()
