from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/math.html")

people_radio = driver.find_element(By.ID, "peopleRule")

print(people_radio.get_attribute("name"))
# Напечатает ruler, т.е. текстовое значение аттрибута

print(people_radio.get_attribute("checked"))
# Напечатает true, т.е. факт того что аттрибут существует.
# true это в данном случае строка, а не булево значение.

print(people_radio.get_attribute("href"))
# Напечатает None, т.к. аттрибут не существует. И это не строка а None-значение.
driver.quit()
