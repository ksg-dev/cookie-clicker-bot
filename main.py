from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# Use this class to use specific keys besides letters/numb
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Identify main components
cookie = driver.find_element(By.ID, value="cookie")
store = driver.find_element(By.ID, value="store")


def check_upgrades():
    store_items = store.find_elements(By.CSS_SELECTOR, value="div")
    for item in store_items[::-1]:
        try:
            item.get_attribute("onclick")
            item.click()
        except:
            pass


timeout = time.time() + 300


def main():
    while time.time() < timeout:
        first_loop = time.time() + 5
        while time.time() < first_loop:
            cookie.click()
        check_upgrades()
    cookies = driver.find_element(By.ID, value="cps").text
    print(cookies)


main()


# driver.quit()

