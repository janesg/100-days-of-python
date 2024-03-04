from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Find a particular anchor tag by CSS selector and click it
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()

# Find anchor by link text
all_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# all_portals.click()

# Find search input by name
search = driver.find_element(By.NAME, "search")
search.send_keys("Python", Keys.ENTER)

# driver.quit()