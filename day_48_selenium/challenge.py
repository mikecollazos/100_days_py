from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

URL = "https://secure-retreat-92358.herokuapp.com/"


driver.get(URL)


first_name = driver.find_element(By.CSS_SELECTOR, 'input[name="fName"]')
first_name.send_keys("Mike")

last_name = driver.find_element(By.CSS_SELECTOR, 'input[name="lName"]')
last_name.send_keys("Mike")

email_address = driver.find_element(By.CSS_SELECTOR, 'input[name="email"]')
email_address.send_keys("Mike@mike.com")

submit = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
submit.send_keys(Keys.ENTER)

# driver.quit()

