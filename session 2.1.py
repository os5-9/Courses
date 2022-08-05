from selenium import webdriver
import math


def calc(z):
  return str(math.log(abs(12*math.sin(int(z)))))


driver = webdriver.Chrome()
driver.get("https://suninjuly.github.io/math.html")

x_element = driver.find_element_by_id("input_value")
x = x_element.text

answer = calc(x)

answer_box = driver.find_element_by_id("answer")
answer_box.send_keys(answer)

driver.find_element_by_css_selector("[for='robotCheckbox']").click()
driver.find_element_by_css_selector("[for='robotsRule']").click()
driver.find_element_by_css_selector("[type='submit']").click()
