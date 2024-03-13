import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


RENTAL_SEARCH_URL = "https://appbrewery.github.io/Zillow-Clone/"
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLScbyFSS77-fn9Ts9t3DxSWqZGF3WS6Utegx413VXPV7OjbePw/viewform?usp=sf_link"


def clean_price(styled_price: str) -> str:
    if len(styled_price.split("+")) > 1:
        return styled_price.split("+")[0]
    elif len(styled_price.split("/")) > 1:
        return styled_price.split("/")[0]
    else:
        return styled_price


def clean_address(styled_addr: str) -> str:
    return styled_addr.strip().replace(" |", ",")


response = requests.get(RENTAL_SEARCH_URL)
soup = BeautifulSoup(response.text, features="html.parser")

addresses = [clean_address(addr.get_text()) for addr in soup.select("address")]
prices = [clean_price(price.get_text()) for price in soup.select("span.PropertyCardWrapper__StyledPriceLine")]
links = [link.get("href") for link in soup.select("a.StyledPropertyCardDataArea-anchor")]

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--headless=new") # for Chrome >= 109

driver = webdriver.Chrome(options=chrome_options)

try:
    for idx in range(0, len(links)):
        # Get form each time to avoid handling navigation back to form after submit takes us to response page
        driver.get(FORM_URL)

        # Rather than hard-code an explicit sleep period, wait for the submit button to become clickable
        submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')))

        # Get all 3 answer inputs with 1 call
        inputs = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[type='text']")))

        inputs[0].send_keys(addresses[idx])
        inputs[1].send_keys(prices[idx])
        inputs[2].send_keys(links[idx])
        submit_button.click()

except Exception as e:
    print(f"Exception: {str(e)}")
finally:
    driver.quit()
