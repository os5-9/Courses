from selenium import webdriver

driver = webdriver.Chrome()
cookies = driver.get_cookies()
print(f"main: cookies = {cookies}")
driver.delete_all_cookies()
driver.quit()
