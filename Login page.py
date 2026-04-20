from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

# Open website
driver.get("https://www.saucedemo.com/")
time.sleep(2)

# Find username
username = driver.find_element(By.ID, "user-name")
time.sleep(1)

# Enter username
username.send_keys("standard_user")
time.sleep(1.5)

# Find password
password = driver.find_element(By.ID, "password")
time.sleep(1)

# Enter password
password.send_keys("secret_sauce")
time.sleep(1.5)

# Click login
login_button = driver.find_element(By.ID, "login-button")
login_button.click()
time.sleep(3)

# Click add to cart
add_to_cart = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
add_to_cart.click()
time.sleep(2)

print("Automation complete!")

# Close browser
driver.quit()