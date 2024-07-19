from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

URL = "https://www.python.org"

driver.get(URL)
event_time_list = driver.find_elements(By.CSS_SELECTOR, value=".event-widget ul time")
event_name_list = driver.find_elements(By.CSS_SELECTOR, value=".event-widget ul a")


event_dict = {}
counter=0
for time, name in zip(event_time_list, event_name_list):
    event_dict[counter] = {"time": time.text, "name": name.text}
    counter+=1
    
print(event_dict)


"""Find elements in python.org """
# URL = "https://www.python.org"
# driver.get(URL)
# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))

# search_button = driver.find_element(By.ID, value="submit")
# print(search_button.size)

# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a" )
# print(documentation_link.text)
# # driver.close()

# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')

# print(bug_link.text)

driver.quit()



"""Get Amazon Pot price element"""

# URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
# driver.get(URL)

# print_dollar = driver.find_element(By.CLASS_NAME, value='a-price-whole')
# print_cents = driver.find_element(By.CLASS_NAME, value='a-price-fraction')

# print(f"The price is {print_dollar.text}.{print_cents.text}")