import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome()
browser.get("https://testautomationpractice.blogspot.com/")
browser.maximize_window()
time.sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
# browser.find_element(By.XPATH,value="//input[@id='sunday']").click()
# time.sleep(5)
# browser.find_element(By.XPATH,value="//input[@id='sunday']").click()
# time.sleep(5)
checkboxes=browser.find_elements(By.XPATH,value="//input[@type='checkbox']")
for checkbox in checkboxes:
    checkbox.send_keys(Keys.SPACE)

checked_count=0
for checkbox in checkboxes:
    if checkbox.is_selected():
        checked_count+=1
expected_checked_count=12
if checked_count == expected_checked_count:
    print("Checkbox count verified")
else:
    print("Checkbox count not verified")
    time.sleep(5)