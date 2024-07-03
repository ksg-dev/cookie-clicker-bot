from selenium import webdriver
from selenium.webdriver.common.by import By
# Use this class to use specific keys besides letters/numb
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Identify main components
cookie = driver.find_element(By.ID, value="cookie")
store = driver.find_element(By.ID, value="store")

# Store Items
# buy_cursor = driver.find_element(By.ID, value="buyCursor")
store_items = store.find_elements(By.CSS_SELECTOR, value="div b")
for item in store_items:
    print(item.text)


def check_upgrades():
    pass
# print(buy_cursor.get_attribute("class"))



# cookie.click()
