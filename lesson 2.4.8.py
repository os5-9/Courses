from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import math


def calculation(z):
  return str(math.log(abs(12*math.sin(int(z)))))


driver = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
driver.get(link)

price_box = WebDriverWait(driver, 12).until(ec.text_to_be_present_in_element((By.ID, "price"), "$100"))
driver.find_element(By.ID, "book").click()

x = driver.find_element(By.ID, "input_value").text

answer = calculation(x)

answer_box = driver.find_element(By.ID, "answer")
answer_box.send_keys(answer)

driver.find_element(By.ID, "solve").click()

time.sleep(20)
driver.quit()
