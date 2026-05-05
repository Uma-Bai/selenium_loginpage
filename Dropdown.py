import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
browser = webdriver.Chrome()
login_url="https://the-internet.herokuapp.com/dropdown"
browser.get(login_url)
browser.maximize_window()
time.sleep(1)
dropdown_element=browser.find_element(By.ID,value="dropdown")
select=Select(dropdown_element)
time.sleep(5)
# select.select_by_visible_text("Option 1")
#time.sleep(1)
# select.select_by_visible_text("Option 2")
#time.sleep(1)
# select.select_by_index(1)
# time.sleep(1)
# select.select_by_index(2)
# time.sleep(2)

select.select_by_value("1")
time.sleep(2)
select.select_by_value("2")
time.sleep(2)
