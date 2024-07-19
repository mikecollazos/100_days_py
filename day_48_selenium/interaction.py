from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

URL = "https://en.wikipedia.org/wiki/Main_Page"


driver.get(URL)
# article_count = driver.find_element(By.CSS_SELECTOR, 'a[href="/wiki/Special:Statistics"]')

# print(article_count.text)

# article_count.click()

# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()


q_button = driver.find_element(By.CSS_SELECTOR, "span.vector-icon.mw-ui-icon-search.mw-ui-icon-wikimedia-search")
q_button.click()

time.sleep(2)

search = driver.find_element(By.CSS_SELECTOR, 'input.cdx-text-input__input')
search.send_keys("Python", Keys.ENTER)




driver.quit()

