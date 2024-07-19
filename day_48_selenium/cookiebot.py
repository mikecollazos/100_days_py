from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

URL = "https://orteil.dashnet.org/experiments/cookie/"


driver.get(URL)


cookie_button  = driver.find_element(By.ID, value='cookie')

# Get upgrade item ids.
items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 60*5
five_sec = time.time() + 5
while timeout > time.time():
    cookie_button.click()

    if time.time() >= five_sec:
        five_sec = time.time() + 5
        all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
        item_prices = []
        # Convert <b> text into an integer price.
        for price in all_prices:
            element_text = price.text
            try:
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)
            except Exception as e:
                print(e)
            # if element_text != "":
            #     cost = int(element_text.split("-")[1].strip().replace(",", ""))
            #     item_prices.append(cost)

        #get current cookie count
        money_element = driver.find_element(By.ID, value='money').text
        if "," in money_element:
            money_element = money_element.replace(",","").strip()
        cookie_count = int(money_element)

        #create dictionary for items available for purchase
        cookie_upgrade = {}
        for n in range(len(item_prices)):
            cookie_upgrade[item_ids[n]] = item_prices[n]

        #create dictionary of items that can be purchased with current cookie count
        affordable_dict = {}
        for upgrade, cost in cookie_upgrade.items():
            if cost < cookie_count:
                affordable_dict[upgrade] = cost            

        # find largest item in dictionary
        try:
            largest_item = max(affordable_dict, key=affordable_dict.get)
            #purchase largest item item in store
            driver.find_element(by=By.ID, value=largest_item).click()
        except Exception as e:
            print(e)

        print(largest_item)


    
cookie_per_s = driver.find_element(by=By.ID, value="cps").text
print(f"the cookie count is {cookie_count}")
print(f"cookie per seconds is {cookie_per_s}")

# driver.quit()

