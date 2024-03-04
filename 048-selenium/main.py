from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep the browser open when program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.co.uk/Applicator-Containers-Moustache-Stencils-Painless/dp/B09DS9BC4W")
price = float(f"{driver.find_element(By.CLASS_NAME, 'a-price-whole').text}." + \
              f"{driver.find_element(By.CLASS_NAME, 'a-price-fraction').text}")
print(f"My nasal waxing kit is: £{price}")
# Close the current tab
# driver.close()

# Close the entire browser
driver.quit()