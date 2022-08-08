from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/selects1.html")

x_element = driver.find_element(By.ID, "num1")
x = int(x_element.text)

y_element = driver.find_element(By.ID, "num2")
y = int(y_element.text)

answer = x + y
print("answer is" + str(answer))

select = Select(driver.find_element(By.TAG_NAME, "select"))
select.select_by_visible_text(str(answer))

driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

time.sleep(10)
driver.quit()
