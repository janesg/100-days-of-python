from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://python.org")

event_li_list = driver.find_elements(By.CSS_SELECTOR, ".event-widget li")

events = {}

for idx in range(0, len(event_li_list)):
    events[idx] = {
        'time': event_li_list[idx].find_element(By.TAG_NAME, "time").get_attribute("datetime").split("T")[0],
        'name': event_li_list[idx].find_element(By.TAG_NAME, "a").text
    }

pprint(events, sort_dicts=False)

# Close the entire browser
driver.quit()
