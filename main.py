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
# store_items = store.find_elements(By.CSS_SELECTOR, value="div b")
# for item in store_items:
#     print(item.text)


def check_upgrades():
    store_items = store.find_elements(By.CSS_SELECTOR, value="div")
    for item in store_items[7::-1]:
        status = item.get_attribute("class")
        item_title = item.find_element(By.CSS_SELECTOR, value="b").text
        name = item_title.split(" - ")
        print(name)
        # print(name)
        # print(price)
        # if status != "grayed":


check_upgrades()
# print(buy_cursor.get_attribute("class"))


driver.quit()
# cookie.click()
